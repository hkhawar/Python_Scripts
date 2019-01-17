%matplotlib inline
import glob
import numpy
import os
import os.path
import pandas
import re
import skimage
import skimage.io
import skimage.transform
import skimage.external
from tqdm._tqdm_notebook import tqdm_notebook
from tqdm import tqdm
import re
import fnmatch
from PIL import Image
from pathlib import Path

import matplotlib.pyplot


imgpath = '/Users/habbasi/Desktop/Output_pad_rescale/'
outdir = '/Users/habbasi/Desktop/Composite/'
os.chdir(imgpath)
# if not os.path.exists(outdir):
#     os.makedirs(outdir)


mglist = glob.glob('*.tif')
imglist

img1=[f for f in imglist if re.match("^.*_ch_0_scale2"  , f)]

for f in tqdm(img1):
#     print(f)
    j = f[:-12] + '1' + f[-11:]
#     print(j)
    image1 = skimage.io.imread(f)
    image2 = skimage.io.imread(j)

    image3 = numpy.expand_dims(image1, axis=2)
#     print(image3.shape)
    image4 = numpy.expand_dims(image2, axis=2)
#     print(image4.shape)
    image5 = numpy.zeros(image3.shape)
    im_composite = numpy.concatenate([image3, image4, image5], axis=2)
#     print(im_composite)
# #         matplotlib.pyplot.imshow(im_composite/numpy.max(im_composite)/256.0)
    filename = "{}_scale2_dna-ecad-composite.TIF".format(f.split('_ch')[0])
#         #skimage.io.imsave(out_dir+ filename ,im_composite)
    skimage.external.tifffile.imsave(os.path.join(outdir, filename), im_composite.astype(numpy.uint8)) 

