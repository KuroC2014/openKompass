from mmengine.config import read_base

with read_base():
    
    from .models.qwen1_5.qwen1_5_0_5b import models

    from .datasets.needlebench.needlebench_32k.needlebench_32k import needlebench_datasets    
    


datasets = [ *needlebench_datasets]



