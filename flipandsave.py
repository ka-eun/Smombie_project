import os
import cv2
import numpy as np


path = "C:\\flipping\\bottle\\"

for i, fname in enumerate(os.listdir(path)):
	imgsrc = path+fname
	img = cv2.imread(imgsrc)
	flip_img = img.copy()
	flip_img = cv2.flip(img, 1)
	#cv2.imshow("horizontal", flip_img)
	result_img = cv2.resize(flip_img, (224, 224)) 
	cv2.imwrite('flipped'+str(i)+'.png', result_img)


