import os
from skimage.color import rgb2lab, lab2rgb, rgb2gray
from skimage.io import imsave
import numpy as np

from PIL import Image


# folder_dir = "C:/Users/nsvro/colorization/original_color/"
# target_dir = "C:/Users/nsvro/colorization/original_bw/"

folder_dir = "C:/Users/nsvro/colorization/kewl_imgs/unsplash_test_og/original/"
target_dir = "C:/Users/nsvro/colorization/kewl_imgs/unsplash_test_og/unsplash_bw/"

for images in os.listdir(folder_dir):
    img = np.asarray(Image.open(os.path.join(folder_dir, images)))
    imsave(os.path.join(target_dir, images),rgb2gray(img))