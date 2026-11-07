"""Build self-contained Kaggle notebooks from the versioned Python sources."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
OWNER='rashmithachamikara'

def build(stage, files, command, gpu=False, sources=()):
    folder=ROOT/'kaggle'/stage; folder.mkdir(parents=True,exist_ok=True)
    setup='from pathlib import Path\n'
    for name in files: setup+=f'Path({name!r}).write_text({(ROOT/name).read_text(encoding="utf-8")!r})\n'
    cells=[dict(cell_type='markdown',metadata={},source=[f'# X03 RDD2022 pilot: {stage}\nPrivate research run. Japan is not used.']),
           dict(cell_type='code',metadata={},execution_count=None,outputs=[],source=[setup]),
           dict(cell_type='code',metadata={},execution_count=None,outputs=[],source=[command])]
    (folder/'run.ipynb').write_text(json.dumps(dict(cells=cells,metadata={'kernelspec':{'display_name':'Python 3','language':'python','name':'python3'}},nbformat=4,nbformat_minor=4)),encoding='utf-8')
    (folder/'kernel-metadata.json').write_text(json.dumps(dict(id=f'{OWNER}/x03-road-{stage}',title=f'X03 Road {stage.title()}',code_file='run.ipynb',language='python',kernel_type='notebook',is_private=True,enable_gpu=gpu,enable_internet=True,dataset_sources=[],kernel_sources=[f'{OWNER}/x03-road-{s}' for s in sources]),indent=2))

if __name__=='__main__':
    build('prepare',['prepare.py'],"import subprocess, sys\nsubprocess.run([sys.executable, '-u', 'prepare.py'], check=True)")
    install="import subprocess, sys\nsubprocess.run([sys.executable, '-m', 'pip', 'install', '-q', 'ultralytics==8.4.192'], check=True)\n"
    for stage, command, sources in [('smoke','smoke',['prepare']),('train','train',['prepare','smoke']),('evaluate','evaluate',['prepare','train'])]:
        # subprocess check=True propagates failures to Kaggle kernel status.
        build(stage,['metrics.py','pilot.py'],install+f"subprocess.run([sys.executable, '-u', 'pilot.py', '{command}'], check=True)",True,sources)
