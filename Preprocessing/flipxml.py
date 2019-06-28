from xml.etree.ElementTree import Element, dump, parse
import os
import cv2
import numpy as np


path = "C:\\Users\\user\\Desktop\\real-darkflow-master\\new_model_data\\Annotations\\"

for i, fname in enumerate(os.listdir(path)):
    tree = parse(fname+'.xml')

    object = tree.find('object')
    bnd = object.find('bndbox')

    # size = object.find('size')
    # width = object.SubElement(size,"width")
    # size.find('width')

    xmin = bnd.find('xmin')
    xmax = bnd.find('xmax')
    # print(xmin.text)

    temp = str(224 - int(xmin.text))
    xmin.text = str(224 - int(xmax.text))
    xmax.text = temp

    # xmin.text = int(width.text)-int(xmin.text)
    tree.write("fname.xml")
    # print(int(xmin,16))
    # note = tree.getroot()

    # xmin_tags = note.findall('object/xmin')

    # print(xmin_tags.items())
