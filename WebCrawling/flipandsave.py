import os
import cv2
import numpy as np


path = "C:\\test\\new1\\"

for i, fname in enumerate(os.listdir(path)):
   imgsrc = path+fname
   img = cv2.imread(imgsrc)
   flip_img = img.copy()
   flip_img = cv2.flip(img, 1)
   #cv2.imshow("Flipped", flip_img)
   cv2.imwrite('flipped'+str(i)+'.png', flip_img)
