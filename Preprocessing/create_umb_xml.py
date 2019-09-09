import os
import cv2
from lxml import etree
import xml.etree.cElementTree as ET

path = 'C:\\Users\\gpffj\\Desktop\\Jiyun\\Project\\Training\\real-darkflow-master\\new_images\\'
savedir = 'annotations_umbrella'


for i, fname in enumerate(os.listdir(path)):

    if not os.path.isdir(savedir):
        os.mkdir(savedir)

    image = cv2.imread(path+fname)
    height, width, depth = image.shape

    annotation = ET.Element('annotaion')
    ET.SubElement(annotation, 'folder').text = path
    ET.SubElement(annotation, 'filename').text = fname
    ET.SubElement(annotation, 'segmented').text = '0'
    size = ET.SubElement(annotation, 'size')
    ET.SubElement(size, 'width').text = str(width)
    ET.SubElement(size, 'height').text = str(height)
    ET.SubElement(size, 'depth').text = str(depth)

    obj = 'umbrella'

    ob = ET.SubElement(annotation, 'object')
    ET.SubElement(ob, 'name').text = obj
    ET.SubElement(ob, 'pose').text = 'Unspecified'
    ET.SubElement(ob, 'truncated').text = '0'
    ET.SubElement(ob, 'difficult').text = '0'
    bbox = ET.SubElement(ob, 'bndbox')
    ET.SubElement(bbox, 'xmin').text = str(0)
    ET.SubElement(bbox, 'ymin').text = str(0)
    ET.SubElement(bbox, 'xmax').text = str(width)
    ET.SubElement(bbox, 'ymax').text = str(height)

    xml_str = ET.tostring(annotation)
    root = etree.fromstring(xml_str)
    xml_str = etree.tostring(root, pretty_print=True)

    save_path = os.path.join(savedir, fname.replace('jpg', 'xml'))
    with open(save_path, 'wb') as temp_xml:
        temp_xml.write(xml_str)


