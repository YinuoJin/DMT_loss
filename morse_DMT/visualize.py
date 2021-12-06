#!/usr/bin/env python

import os 
import sys
import numpy as np
from skimage import io

args = sys.argv
assert len(args) == 3, "Please specify vert output file"

fname = os.path.join(os.getcwd(), args[-2])
mask_name = args[-1]
out_path = fname.rpartition('/')[0]
assert os.path.exists(fname), "Vert output file doesn't exist"

vert_out = np.loadtxt(fname).astype(np.int64)
mask = np.zeros(tuple(vert_out.max(0)[:-1]+1))

for i in range(len(vert_out)):
    mask[vert_out[i, 0], vert_out[i, 1], vert_out[i, 2]] = 1

io.imsave(os.path.join(out_path, mask_name), mask)
