"""Sequential budget-gated Kaggle execution; no duplicate submission on reattach."""
import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parent))
from run_pipeline import log,commit
os.environ['PYTHONIOENCODING']='utf-8'
STAGES=['smoke','baseline','generic','small-thin','select','evaluate']

def cli(args,record):
    log('B command: `python -m kaggle '+' '.join(args)+'`')
    p=subprocess.run([sys.executable,'-m','kaggle',*args],capture_output=True,text=True,encoding='utf-8',errors='replace')
    (ROOT/'runs'/record).write_text(p.stdout+'\n'+p.stderr,encoding='utf-8')
    if p.returncode: raise RuntimeError(f'CLI failed: {record}; no automatic job resubmission')
    return p.stdout

def wait(stage):
    last=None; failures=0
    while True:
        p=subprocess.run([sys.executable,'-m','kaggle','kernels','status',f'rashmithachamikara/x03-b-{stage}'],capture_output=True,text=True)
        if p.returncode:
            failures+=1; log(f'B {stage} status-query failure{failures}/5')
            if failures==5: raise RuntimeError('Status unavailable; reattach existing job with --monitor')
            time.sleep(30); continue
        failures=0; state=p.stdout.strip()
        (ROOT/'runs'/f'{stage}-status.txt').write_text(state)
        if state!=last: log(state); print(state,flush=True); last=state
        if 'COMPLETE' in state: return
        if any(x in state for x in ['ERROR','CANCELLED','CANCELED']):
            cli(['kernels','output',f'rashmithachamikara/x03-b-{stage}','-p',str(ROOT/'artifacts'/stage),'--file-pattern','.*(json|log|yaml|csv)$'],f'{stage}-failure-output.txt')
            raise RuntimeError(f'B {stage} failed; inspect artifacts before recovery')
        time.sleep(30)

def run(start,monitor):
    for stage in STAGES[STAGES.index(start):]:
        if stage!='smoke':
            gate=json.loads(next((ROOT/'artifacts/smoke').rglob('budget-gate.json')).read_text())
            assert gate['status']=='passed' and gate['projected_gpu_hours']<=12
        if not (stage==start and monitor):
            response=cli(['kernels','push','-p',str(ROOT/'kaggle'/stage),'--accelerator','NvidiaTeslaT4','-t','21600' if stage in ['baseline','generic','small-thin'] else '7200'],f'{stage}-launch.txt')
            log(response.strip()); print(response.strip(),flush=True)
        wait(stage)
        pattern='.*(json|log|yaml|csv|txt)$' if stage=='smoke' else '.*(json|gz|csv|yaml|log|txt)$|.*-best[.]pt$' if stage in ['baseline','generic','small-thin'] else '.*'
        cli(['kernels','output',f'rashmithachamikara/x03-b-{stage}','-p',str(ROOT/'artifacts'/stage),'--file-pattern',pattern],f'{stage}-download.txt')
        if stage=='smoke':
            gate=json.loads(next((ROOT/'artifacts/smoke').rglob('budget-gate.json')).read_text())
            (ROOT/'runs/budget-gate.json').write_text(json.dumps(gate,indent=2))
            assert gate['status']=='passed' and gate['projected_gpu_hours']<=12,gate
            log('B smoke/recovery passed; budget projection '+str(gate['projected_gpu_hours'])+'h, common batch'+str(gate['batch']))
            commit('Add validated B consistency prototype and budget-gated Kaggle runner')
        if stage=='evaluate':
            subprocess.run([sys.executable,str(ROOT/'b_report.py')],check=True)
            log('B comparison/report completed; one-seed development evidence, not confirmation.')
            commit('Record B prototype comparison and verified diagnostic results')

if __name__=='__main__':
    parser=argparse.ArgumentParser(); parser.add_argument('start',choices=STAGES); parser.add_argument('--monitor',action='store_true'); args=parser.parse_args()
    try: run(args.start,args.monitor)
    except Exception as e: log('B pipeline stopped: '+str(e)); raise
