import os
import cv2
import numpy as np


path = "C:\\Users\\user\\Desktop\\ns_front\\"

for i, fname in enumerate(os.listdir(path)):
    j=i%10
    fullpath = path + fname
    new_name = str(j)+ "ns_front_" + str(i) + ".jpg"
    print(fname, new_name)
    os.rename(path + fname, path + new_name)
