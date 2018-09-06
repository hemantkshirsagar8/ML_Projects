# Created by: Hemant Kshirsagar
# Purpose: To rename all the images in proper sequencese.
# Input: It need image folder path
# Output: It will rename all the images in proper number sequencese.
# Syntax: "python rename_images.py YOUR_IMAGE_FOLDER_PATH"

import os
import sys

try:
    imdir = sys.argv[1]
    n = 0
    for imfile in os.scandir(imdir):
        os.rename(imfile.path, os.path.join(imdir, '{:06}.png'.format(n)))
        n += 1
except IndexError:
    print("Please provide image directory path")
