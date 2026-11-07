"""Sequential private Kaggle launcher; log locally and stop on any failed gate."""
import datetime
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

ROOT=Path(__file__).resolve().parent
OWNER='rashmithachamikara'
os.environ['PYTHONIOENCODING']='utf-8'

def log(message):
    stamp=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=5,minutes=30))).strftime('%Y-%m-%d %H:%M:%S')
    with open(ROOT/'log.md','a',encoding='utf-8') as f: f.write(f'\n- **{stamp} Asia/Colombo** — {message}\n')
    print(message,flush=True)

def cli(args,name):
    cmd=[sys.executable,'-m','kaggle',*args]
    log('Command: `python -m kaggle '+' '.join(args)+'`')
    p=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8',errors='replace')
    (ROOT/'runs'/name).write_text(p.stdout+'\n'+p.stderr,encoding='utf-8')
    if p.returncode: raise RuntimeError(f'Kaggle command failed; see runs/{name}')
    return p.stdout

def wait(stage):
    last=None; failures=0
    while True:
        p=subprocess.run([sys.executable,'-m','kaggle','kernels','status',f'{OWNER}/x03-road-{stage}'],capture_output=True,text=True)
        if p.returncode:
            failures+=1; log(f'Transient status-query failure {failures}/5 for {stage}; no job resubmission.')
            if failures>=5: raise RuntimeError(f'Cannot query {stage}: '+p.stderr[-500:])
            time.sleep(30); continue
        failures=0
        state=p.stdout.strip()
        if state!=last: log(state); last=state
        (ROOT/'runs'/f'{stage}-status.txt').write_text(state)
        if 'COMPLETE' in state: return
        if any(s in state for s in ['ERROR','CANCELLED']):
            cli(['kernels','output',f'{OWNER}/x03-road-{stage}','-p',str(ROOT/'artifacts'/stage),'--file-pattern','.*log$'],f'{stage}-failure-output.txt')
            raise RuntimeError(f'{stage} failed; inspect downloaded log before retrying')
        time.sleep(30)

def commit(message):
    # Explicit project-scoped paths only; never git add -A at repository root.
    log('Creating local project-scoped commit: '+message)
    subprocess.run(['git','add','--',str(ROOT)],check=True)
    staged=subprocess.check_output(['git','diff','--cached','--name-only'],text=True).splitlines()
    if any(not p.startswith('projects/x03-road-damage/') for p in staged):
        raise RuntimeError('Unrelated staged files exist: refusing broad commit')
    subprocess.run(['git','commit','-m',message],check=True)
    print('Local commit: '+subprocess.check_output(['git','rev-parse','--short','HEAD'],text=True).strip()+' — '+message,flush=True)

def run(start='prepare',monitor_existing=False):
    stages=['prepare','smoke','train','evaluate']
    for stage in stages[stages.index(start):]:
        if stage!='prepare' and not (stage==start and monitor_existing):
            response=cli(['kernels','push','-p',str(ROOT/'kaggle'/stage),'--accelerator','NvidiaTeslaT4','-t','43200'],f'{stage}-launch.txt')
            log(response.strip())
        wait(stage)
        pattern='.*(json|jpg|log|csv|yaml)$' if stage=='prepare' else '.*(json|csv|yaml|log|txt)$' if stage=='smoke' else '.*(json|csv|yaml|log|txt)$|(^|/)(best|last)[.]pt$' if stage=='train' else '.*'
        cli(['kernels','output',f'{OWNER}/x03-road-{stage}','-p',str(ROOT/'artifacts'/stage),'--file-pattern',pattern],f'{stage}-download.txt')
        if stage=='prepare':
            audit=next((ROOT/'artifacts/prepare').rglob('audit.json'))
            info=json.loads(audit.read_text()); log('Preparation audit: '+json.dumps(info['counts']))
            for p in (ROOT/'artifacts/prepare').rglob('conversion_*.jpg'): shutil_copy(p,ROOT/'runs'/p.name)
            shutil_copy(audit,ROOT/'runs/audit.json')
        if stage=='smoke':
            p=next((ROOT/'artifacts/smoke').rglob('smoke.json')); info=json.loads(p.read_text()); assert info['status']=='passed'
            shutil_copy(p,ROOT/'runs/smoke.json'); log('Smoke/recovery passed: '+json.dumps(info))
            commit('Add validated X03 Kaggle baseline pilot and recovery test')
        if stage=='train':
            p=next((ROOT/'artifacts/train').rglob('training-complete.json')); log('Training outcome: '+p.read_text())
        if stage=='evaluate':
            subprocess.run([sys.executable,str(ROOT/'report.py')],check=True)
            log('Evaluation complete; wrote pilot-report.md and runs/summary.json. Results are one-seed development evidence.')
            commit('Record X03 Kaggle baseline pilot results and diagnostics')

def shutil_copy(a,b):
    import shutil
    shutil.copy2(a,b)

if __name__=='__main__':
    try: run(sys.argv[1] if len(sys.argv)>1 else 'prepare',monitor_existing='--monitor' in sys.argv[2:])
    except Exception as e: log('Pipeline stopped: '+str(e)); raise
