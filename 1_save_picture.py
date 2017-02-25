#!/usr/bin/env python
import cv2, sys

# Constants
DEVICE_NUMBER = 0
IMAGE_FILE = "output.jpg"

# Init webcam
# http://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html#videocapture-videocapture
vc = cv2.VideoCapture(DEVICE_NUMBER)

# Check if the webcam init was successful
# http://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html#videocapture-isopened
if vc.isOpened(): # try to get the first frame
    # http://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html#videocapture-read
    retval, frame = vc.read()
else:
    # Exit the program
    sys.exit(1)

retval, frame = vc.read()

cv2.imwrite(IMAGE_FILE, frame)

img = cv2.imread(IMAGE_FILE)

# http://docs.opencv.org/2.4/modules/highgui/doc/user_interface.html#imshow
cv2.imshow("DB410c Workshop", img)

# Exit program after waiting indefinitely for a pressed key
# http://docs.opencv.org/2.4/modules/highgui/doc/user_interface.html#waitkey
cv2.waitKey(0)
