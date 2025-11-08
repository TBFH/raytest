import os
import torch

BASE_DIR = os.path.dirname(__file__)
# LIB_DIR = os.path.join(BASE_DIR, "../SwiftTransformer/build/lib")
LIB_DIR = os.path.join(BASE_DIR, "../build/lib_v2")

if not os.path.exists(LIB_DIR):
    raise RuntimeError(
        f"Could not find the SwiftTransformer library libst_pybinding.so at {LIB_DIR}. "
        "Please build the SwiftTransformer library first or put it at the right place."
    )

torch.ops.load_library(os.path.join(LIB_DIR, "libst_pybinding.so"))

from .llm import OfflineLLM
from .request import SamplingParams