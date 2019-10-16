import cv2
from darkflow.net.build import TFNet
import numpy as np
import time
import serial

options = {
    'model': 'cfg/my-yolo-voc.cfg',
    'load': 30625,
    'threshold': 0.3,
    'gpu': 0.8
}

tfnet = TFNet(options)
colors = [tuple(255 * np.random.rand(3)) for _ in range(10)]

sm_flag = 'n'
#알림
arduino = serial.Serial('COM3', 9600)
#신호등
arduino2 = serial.Serial('COM4', 9600)

capture = cv2.VideoCapture(1)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
light = 0
print(light)

light = arduino2.read()

while True:
    stime = time.time()
    ret, frame = capture.read()
    results = tfnet.return_predict(frame)

    if(arduino2.readable()):
        print('here')

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

        arduino2.flushInput()
        light = arduino2.read().decode('utf-8')
        arduino2.flushInput()

        print(light)

        if(light=='1'):
            sm_flag = sm_flag.encode('utf-8')
            arduino.write(sm_flag)
            print(sm_flag)
            sm_flag = 'n'


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()
