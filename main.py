ComputeLB = False

import os, gc, zipfile
import numpy as np, pandas as pd
from PIL import Image
import matplotlib.pyplot as plt

if ComputeLB: PATH = '../input/generative-dog-images/all-dogs/all-dogs/'
else: PATH = '/home/est_posgrado_manuel.suarez/data/all-dogs'
IMAGES = os.listdir(PATH)
print('There are',len(IMAGES),'images. Here are 5 example filesnames:')
print(IMAGES[:5])