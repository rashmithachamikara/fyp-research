import ast
import hashlib
import json
from pathlib import Path

root=Path(__file__).parent
common=(root/'common.py').read_text()
eval_code=common+(root/'evaluate.py').read_text()
digest=hashlib.sha256(eval_code.encode()).hexdigest()
for stage,code,gpu,sources in [
    ('trainval','extract',True,['bicycle-jpeg-ab-rehearsal','bicycle-jpeg-timing-prototype']),
    ('training','train',False,['bicycle-jpeg-ab-rehearsal','bicycle-formal-trainval']),
    ('test','extract',True,['bicycle-jpeg-ab-rehearsal','bicycle-jpeg-timing-prototype','bicycle-formal-training']),
    ('evaluation','evaluate',False,['bicycle-jpeg-ab-rehearsal','bicycle-formal-training','bicycle-formal-test'])]:
    p=root/stage;p.mkdir(exist_ok=True)
    script=f"STAGE={stage!r}\nEVAL_HASH={digest!r}\n"+common+(root/f'{code}.py').read_text()
    ast.parse(script)
    nb=dict(cells=[dict(cell_type='code',metadata={},execution_count=None,outputs=[],source=script.splitlines(keepends=True))],
            metadata=dict(kernelspec=dict(display_name='Python 3',language='python',name='python3')),nbformat=4,nbformat_minor=5)
    (p/'run.ipynb').write_text(json.dumps(nb,indent=2))
    meta=dict(id=f'rashmithachamikara/bicycle-formal-{stage}',title=f'Bicycle Formal {stage.title()}',code_file='run.ipynb',language='python',
              kernel_type='notebook',is_private=True,enable_gpu=gpu,enable_internet=True,dataset_sources=['awsaf49/coco-2017-dataset'],
              kernel_sources=[f'rashmithachamikara/{s}' for s in sources])
    (p/'kernel-metadata.json').write_text(json.dumps(meta,indent=2))
print('Four notebooks validated. Evaluation hash',digest)
