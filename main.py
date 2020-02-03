import cv2
import numpy as np
import pyscreenshot
from pynput.mouse import Button, Controller
from time import sleep
import time
import webbrowser

# URL for the online test
url = "https://www.mouseaccuracy.com/game"

# Initialized the mouse so that I can click
mouse = Controller()

# Creating a basic blob detector and setting parameters.
params = cv2.SimpleBlobDetector_Params()
params.filterByCircularity = True
params.minCircularity = 0.1
detector = cv2.SimpleBlobDetector_create(params)

# Open the mouse test
webbrowser.open(url)

# Chill for 3 seconds while the game loads
sleep(2.5)

# Initiate a current time variable to measure run time
startTime = time.time()

while(True):

    # Checks to see if run time has been 30 seconds
    if time.time() - startTime > 31:
        break

    # Grabbed the screen and crop out the necessary portion of the screen.
    img = pyscreenshot.grab()
    data = np.asarray(img)
    img2 = data[172:1080, 0:1920]

    # Put the threshold on the image to make blob detection easier
    ret, threshHeld = cv2.threshold(img2, 4, 255, cv2.THRESH_BINARY)

    # Search for all of the blobs on screen and store it to the variable keypoints
    keypoints = detector.detect(threshHeld)

    # Iterates through all of the blobs and clicks on them.
    for point in keypoints:
        mouse.position = (point.pt[0], point.pt[1] + 172)
        mouse.click(Button.left, 1)

    # Chill for 70 milliseconds so it doesn't click too quickly
    sleep(.07)

