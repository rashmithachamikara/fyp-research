"""Self-contained private Kaggle notebooks; original preparation/COCO inputs reused."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent; PROJECT=ROOT.parent; OWNER='rashmithachamikara'

def build(stage,command,sources):
    folder=ROOT/'kaggle'/stage; folder.mkdir(parents=True,exist_ok=True)
    setup='from pathlib import Path\n'
    for name in ['b_core.py','b_run.py','test_b_core.py','experiment.json']:
        setup+=f'Path({name!r}).write_text({(ROOT/name).read_text(encoding="utf-8")!r})\n'
    for name in ['metrics.py','pilot.py']:
        setup+=f'Path({name!r}).write_text({(PROJECT/name).read_text(encoding="utf-8")!r})\n'
    cells=[dict(cell_type='markdown',metadata={},source=[f'# B prototype: {stage}\nDevelopment evidence only. Japan untouched.']),
           dict(cell_type='code',metadata={},execution_count=None,outputs=[],source=[setup]),
           dict(cell_type='code',metadata={},execution_count=None,outputs=[],source=["import subprocess,sys\nsubprocess.run([sys.executable,'-m','pip','install','-q','ultralytics==8.4.192'],check=True)\n"+f"subprocess.run([sys.executable,'-u','b_run.py',*{command!r}],check=True)\n"])]
    (folder/'run.ipynb').write_text(json.dumps(dict(cells=cells,metadata={'kernelspec':{'display_name':'Python 3','language':'python','name':'python3'}},nbformat=4,nbformat_minor=4)),encoding='utf-8')
    (folder/'kernel-metadata.json').write_text(json.dumps(dict(id=f'{OWNER}/x03-b-{stage}',title=f'X03 B {stage.title()}',code_file='run.ipynb',language='python',kernel_type='notebook',is_private=True,enable_gpu=True,enable_internet=True,dataset_sources=[],kernel_sources=[OWNER+'/'+s for s in sources]),indent=2))

if __name__=='__main__':
    original=['x03-road-prepare','x03-road-train']
    build('smoke',['smoke'],original)
    for arm in ['baseline','generic','small_thin']:
        build(arm.replace('_','-'),['train','--arm',arm],original+['x03-b-smoke'])
    trained=['x03-road-prepare','x03-b-baseline','x03-b-generic','x03-b-small-thin']
    build('select',['select'],trained)
    build('evaluate',['evaluate'],trained+['x03-b-select'])
