import cv2
import numpy as np
import pyscreenshot
from pynput.mouse import Button, Controller
from time import sleep
import time
import webbrowser

url = "https://www.mouseaccuracy.com/game"

mouse = Controller()

params = cv2.SimpleBlobDetector_Params()
params.filterByCircularity = True
params.minCircularity = 0.1
detector = cv2.SimpleBlobDetector_create(params)

startTime = time.time()

webbrowser.open(url)

sleep(3)

while(True):
    if time.time() - startTime > 34:
        break

    img = pyscreenshot.grab()
    data = np.asarray(img)
    img2 = data[140:1080, 0:1920]
    ret, threshHeld = cv2.threshold(img2, 4, 255, cv2.THRESH_BINARY)

    keypoints = detector.detect(threshHeld)
    for point in keypoints:
        mouse.position = (point.pt[0], point.pt[1] + 140)
        mouse.click(Button.left, 1)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
# driver.close()