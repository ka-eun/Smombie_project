import cv2
from darkflow.net.build import TFNet
import numpy as np
import time
import serial

options = {
    'model': 'cfg/my-yolo-voc.cfg',
    'load': 31625,
    'threshold': 0.175,
    'gpu': 0.8
}

tfnet = TFNet(options)
colors = [tuple(255 * np.random.rand(3)) for _ in range(10)]


"""
image = cv2.imread('new_model_data\\smombie\\1imgAI269_t.png')
#image.resize(cv2.CAP_PROP_FRAME_WIDTH, 1920)
#image.set(cv2.CAP_PROP_FRAME_HEIGTH, 1080)
arduino = serial.Serial('COM4', 9400)

frame = image
ret = True
sm_flag = 0
results = tfnet.return_predict(frame)
if ret:
    for color, result in zip(colors, results):
        tl = (result['topleft']['x'], result['topleft']['y'])
        br = (result['bottomright']['x'], result['bottomright']['y'])
        label = result['label']
        confidence = result['confidence']
        text = '{}: {:.0f}%'.format(label, confidence * 100)
        frame = cv2.rectangle(frame, tl, br, color, 5)
        frame = cv2.putText(frame, text, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)

        if label=='smombie':
            sm_flag = 1
        else :
            sm_flag = 0

    cv2.imshow('frame', frame)
    arduino.write(sm_flag)


    key = cv2.waitKey(300000)#pauses for 3 seconds before fetching next image


"""

sm_flag = 'n'
arduino = serial.Serial('COM4', 9600)

capture = cv2.VideoCapture(1)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

while True:
    stime = time.time()
    ret, frame = capture.read()
    results = tfnet.return_predict(frame)
    if ret:
        for color, result in zip(colors, results):
            tl = (result['topleft']['x'], result['topleft']['y'])
            br = (result['bottomright']['x'], result['bottomright']['y'])
            label = result['label']
            confidence = result['confidence']
            text = '{}: {:.0f}%'.format(label, confidence*100)
            frame = cv2.rectangle(frame, tl, br, color, 5)
            frame = cv2.putText(frame, text, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)

            if label == 'smombie':
                sm_flag = 's'

        cv2.imshow('frame', frame)
        print('FPS {:.1f}'.format(1/(time.time()-stime)))

    sm_flag = sm_flag.encode('utf-8')
    arduino.write(sm_flag)
    print(sm_flag)
    sm_flag = 'n'

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()
