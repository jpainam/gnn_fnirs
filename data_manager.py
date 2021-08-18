import torch
import torchvision
import torchvision.transforms as transforms
from PIL import Image
import os.path as osp
from torch.utils.data.dataset import T_co
from torchvision.transforms.transforms import ToTensor, Lambda, Normalize
from collections import defaultdict
import numpy as np

import os
import pickle
from torch.utils.data import Dataset


class FNIRSDataset(Dataset):
    def __init__(self, folder, transform=None):

        self.X
        self.Y

    def __len__(self):
        return
    def __getitem__(self, index) -> T_co:
        pass
