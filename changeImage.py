#!/usr/bin/env python3
from PIL import Image
import os
#This is the path where the images and txt files are located
path = "./supplier-data/images/"

for f in os.listdir(path):
    #checking if the image ends with .tiff , we will replace it with .jepg
    if f.endswith(".tiff"):
        split_f = f.split(".")
        name = split_f[0] + ".jpeg"
        im = Image.open(path + f).convert("RGB")
        #resizing the images and saving them in the same directory
        im.resize((600, 400)).save(path + name, "JPEG")


