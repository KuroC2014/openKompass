from opencompass.models import HuggingFaceCausalLM
models = [
    # qwen 1.5
    dict(
        type=HuggingFaceCausalLM,
        abbr='myQwen1.5',
        path="models/qwen1.5_0.5b/Qwen1.5-0.5B", 
        tokenizer_path="models/qwen1.5_0.5b/Qwen1.5-0.5B", 
        tokenizer_kwargs=dict(padding_side='left',
                              truncation_side='left',
                              use_fast=False,
                              ),
        max_out_len=100,
        max_seq_len=2048,
        batch_size=8,
        model_kwargs=dict(device_map='auto'),
        batch_padding=False, # if false, inference with for-loop without batch padding
        run_cfg=dict(num_gpus=1, num_procs=1),
    )
]
