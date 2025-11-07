import torch
import d2l
print("PyTorch 版本:", torch.__version__)
print("d2l 版本:", d2l.__version__)
print("CUDA 是否可用:", torch.cuda.is_available())  # 应返回 False，因为安装的是CPU版本