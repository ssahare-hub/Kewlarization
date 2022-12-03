import os
import numpy as np
from image_similarity_measures.quality_metrics import rmse, psnr, ssim, fsim, uiq
from PIL import Image

# original = "C:/Users/nsvro/colorization/original_color/"
# colorized = "C:/Users/nsvro/colorization/colorized_bw/"

original = "C:/Users/nsvro/colorization/kewl_imgs/unsplash_test_og/original/"
colorized = "C:/Users/nsvro/colorization/kewl_imgs/unsplash_test_og/unsplash_cic/"

for image in os.listdir(original):
    print(image)
    og_img = Image.open(os.path.join(original, image))
    og_img = og_img.resize((512,512))
    og_img = 1.0 / 255 *np.asarray(og_img)
    col_img = Image.open(os.path.join(colorized, image))
    col_img = col_img.resize((512,512))
    col_img = 1.0 / 255 *np.asarray(col_img)
    img_rmse = rmse(og_img, col_img)
    img_psnr = psnr(og_img, col_img)
    img_fsim = fsim(og_img, col_img)
    img_uiq = uiq(og_img, col_img)
    print(f' RSME {img_rmse} PSNR {img_psnr} FSIM {img_fsim} UIQ {img_uiq}')