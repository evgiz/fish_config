
# [path] [rows] [limit] [contains]
 
"""
Date: January, 2019
Author: Sigve Rokenes

Util for combining multiple images into a single collage. Note that the images must be the same size!
Useful for generating collages from the results of a GAN or other machine learning algorithms.

Usage:

    $ collage.py [path] [rows] [limit] [contains]

    path:        directory with images
    rows:        number of rows in collage
    limit:       max number of images
    contains:    only include images with keyword

"""

import sys
import os
import skimage as sk
from skimage import io
from skimage import exposure
import numpy as np


# ============================ #
#      Generate collage        #
# ============================ #

def create_collage(c_images, c_rows):
    collage = []
    images_per_row = int(np.ceil(len(c_images) / float(c_rows)))
    for img_row in range(c_rows):
        current_images = c_images[img_row * images_per_row:img_row * images_per_row + images_per_row]
        while len(current_images) < images_per_row:
            current_images.append(np.full(c_images[0].shape, 255, dtype=np.uint8))
        for pixel_row in range(c_images[0].shape[0]):
            c_row = []
            for c_img in current_images:
                for x in c_img[pixel_row]:
                    c_row.append(x)
            collage.append(c_row)
    return np.array(collage)


# ============================ #
#      Command line tool       #
# ============================ #

if __name__ == "__main__":

    path = os.getcwd()
    if len(sys.argv) > 1:
        path = sys.argv[1]
    output = os.path.join(path, "collage.png")
    rows = 1
    contains = ""
    limit = 512

    if len(sys.argv) > 3:
        try:
            limit = int(sys.argv[3])
            rows = min(limit, 512)
        except ValueError:
            print("<limit> must be an integer")
            limit = 512
        if limit <= 0:
            limit = 512
    if len(sys.argv) > 2:
        try:
            rows = int(sys.argv[2])
            rows = min(limit, rows)
        except ValueError:
            print("<rows> must be an integer")
            rows = 1
    if len(sys.argv) > 4:
        contains = sys.argv[4]

    if not os.path.isdir(path):
        print("Directory", path, "not found")
        exit(-1)

    # ============================ #
    #    Load images from folder   #
    # ============================ #

    image_paths = os.listdir(path)
    removed = 0
    images = []

    for p in image_paths:
        if not p.endswith(".png") and not p.endswith(".gif"):
            continue
        if contains not in p:
            continue
        if "collage" in p:
            continue
        img = sk.io.imread(os.path.join(path, p))
        if sk.exposure.is_low_contrast(img):
            continue
        print(p)
        images.append(img)
        if img.shape != images[0].shape:
            print("Error: image", p, "is not the same shape.")
            exit(-1)
        if len(images) == limit:
            break

    if len(images) == 0:
        print("No images found in directory", path)
        exit(0)

    result = create_collage(images, rows)
    sk.io.imsave(output, result)
    print("collage created.")