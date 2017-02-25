#!/usr/bin/env python
import cv2, sys

# Constants
DEVICE_NUMBER = 0
FONT_FACES = [
	cv2.FONT_HERSHEY_SIMPLEX,
	cv2.FONT_HERSHEY_PLAIN,
	cv2.FONT_HERSHEY_DUPLEX,
	cv2.FONT_HERSHEY_COMPLEX,
	cv2.FONT_HERSHEY_TRIPLEX,
	cv2.FONT_HERSHEY_COMPLEX_SMALL,
	cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,
	cv2.FONT_HERSHEY_SCRIPT_COMPLEX
]

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


while retval:
	font_typeface = FONT_FACES[5]
	font_scale = 2
	font_color = (0,0,255)
	font_weight = 5
	x = 0
	y = 50
	cv2.putText(frame,"[LIVE]",(x,y),
		font_typeface,font_scale,font_color,font_weight)


# http://docs.opencv.org/2.4/modules/highgui/doc/user_interface.html#imshow
	cv2.imshow("DB410c Workshop", frame)

	retval, frame = vc.read()

# Exit program after waiting indefinitely for a pressed key
# http://docs.opencv.org/2.4/modules/highgui/doc/user_interface.html#waitkey
	if cv2.waitKey(1) == 27:
		break
