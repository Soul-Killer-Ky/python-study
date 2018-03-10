# -*- coding=utf-8 -*-

import os
from PIL import Image

pathDir = "D:/Personal/Documents/Tencent Files/1024718314/FileRecv"
newPathDir = "H:/code/python/private/20180227-1/img/"
os.chdir(pathDir)

def get_image_list():
    img_list = []
    list_dir = os.listdir(pathDir)
    for i in list_dir:
        if '.jpg' in i or '.png' in i:
            img_list.append(i)
        # else:
            # print("This is not a picture: " + i)
    print(img_list)
    return img_list

if __name__ == "__main__":
    for filename in get_image_list():
        # print(filename)
        with Image.open(filename) as img:
            if max(img.size) > 1136:
                print(filename)
                value = max(img.size) / 1136.0
                new_size_min = min(img.size) / value
                new_img = img.resize((1136, int(new_size_min)), Image.ANTIALIAS)
                new_img.save(newPathDir + 'new_' + filename)
