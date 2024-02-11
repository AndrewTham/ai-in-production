#!/bin/bash

python -c "import torch; print(f'CUDA {\"is\" if torch.cuda.is_available() else \"not\"} available');"

uvicorn --host 0.0.0.0 --port $PORT main:app