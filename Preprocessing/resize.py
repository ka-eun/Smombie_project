import os
import cv2
import numpy as np


path = "C:\\Users\\user\\Desktop\\ns_front\\"

for i, fname in enumerate(os.listdir(path)):
	imgsrc = path+fname
	img = cv2.imread(imgsrc)
	resize_img = img.copy()
	dim = (224, 224)
	resize_img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
	# cv2.imshow("horizontal", resize_img)
	cv2.imwrite(path+fname, resize_img)
