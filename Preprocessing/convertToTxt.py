from xml.etree.ElementTree import Element, dump, parse
import os
import cv2
import numpy as np

path = "C:\\Users\\gpffj\\Desktop\\Jiyun\\Project\\Training\\real-darkflow-master\\Annotations\\"


for i, fname in enumerate(os.listdir(path)):
    tree = parse(path+fname)
    f = open("C:\\Users\\gpffj\\Desktop\\Jiyun\\Project\\Training\\real-darkflow-master\\textfile\\"+fname[:-4]+".txt", 'w', encoding='utf8')

    for object in tree.findall('object'):
        bnd = object.find('bndbox')

        xmin = bnd.find('xmin')
        xmax = bnd.find('xmax')
        ymin = bnd.find('ymin')
        ymax = bnd.find('ymax')

        absolute_height = int(ymax.text)-int(ymin.text)
        absolute_width = int(xmax.text)-int(xmin.text)
        absolute_x = (int(xmax.text)+int(xmin.text))/2.0
        absolute_y = (int(ymax.text)+int(ymin.text))/2.0

        height = absolute_height/224.0
        width = absolute_width/224.0
        x = absolute_x/224.0
        y = absolute_y/224.0

        data = "0 "+str(x)+" "+str(y)+" "+str(width)+" "+str(height)
        f.write(data)
        
    f.close()

        
