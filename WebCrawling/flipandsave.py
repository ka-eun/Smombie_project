import os
import cv2
import numpy as np


path = "C:\\resizing\\"

for i, fname in enumerate(os.listdir(path)):
	imgsrc = path+fname
	img = cv2.imread(imgsrc)
	resize_img = img.copy()
	dim = (32, 32)
	resize_img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
	cv2.imshow("horizontal", resize_img)
	cv2.imwrite('flipped'+str(i)+'.png', resize_img)


