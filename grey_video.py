import cv2
import numpy as np
import os
import time

filename = 'harsh.avi'
f_p_s = 24.0
res = '720p'


def resize_accordingly(cam,height,width):
	cam.set(3,width)
	cam.set(4,height)


STD_DIMENSIONS = {
	"480p": (640,480),
	"720p": (1280,720),
	"1080p": (1920,1080),
	"4k": (3840,2160),
}

#get resolutions dimensions and set video capture to it.
def get_dims(cap, res='720p'):
	width, height = STD_DIMENSIONS["480p"]
	if res in STD_DIMENSIONS:
		width,height = STD_DIMENSIONS[res]
	#to the resulting resolution
	resize_accordingly(cam,width,height)
	return width,height


# Video Encoding, might require additional installs

VIDEO_TYPE = {
    'avi': cv2.VideoWriter_fourcc(*'XVID'),
    #'mp4': cv2.VideoWriter_fourcc(*'H264'),
    'mp4': cv2.VideoWriter_fourcc(*'XVID'),
}

def get_video_type(filename):
    filename, ext = os.path.splitext(filename)
    if ext in VIDEO_TYPE:
      return  VIDEO_TYPE[ext]
    return VIDEO_TYPE['avi']


def resize_1080p():
	cam.set(3,1920)
	cam.set(4,1080)

def resize_720p():
	cam.set(3,1280)
	cam.set(4,720)

def resize_480p():
	cam.set(3,640)
	cam.set(4,480)

cam = cv2.VideoCapture(0)
out = cv2.VideoWriter(filename,get_video_type(filename),15,get_dims(cam, res))
cv2.namedWindow("test")

def main(img_counter = 1):
	resize_1080p()



	ret, frame = cam.read()
	#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)		#for converting into gray color
	#sketch_gray, sketch_color = cv2.pencilSketch(frame, sigma_s=60, sigma_r=0.07, shade_factor=0.05) 	#for converting into sketch and sketch colour

	cv2.imshow("test", frame)
	#out.write(frame)			//video wala
	img_name = "{}.png".format(img_counter)
	path = '/root/Documents/miniProject/ML Part/facial_recogn/test'
	cv2.imwrite(os.path.join(path , img_name), frame)
	#cv2.imwrite(img_name, frame)
	print("{} written!".format(img_name))
	#img_counter += 1


	#cv2.imshow("gray", gray)
	#cv2.imshow("sketch_gray", sketch_gray)
	#cv2.imshow("sketch_color", sketch_color)

	# if not ret:
	# 	break
	#
	#

	# elif k%256 == 32:
	# 	# SPACE pressed
	# 	img_name = "opencv_frame_{}.png".format(img_counter)
	# 	cv2.imwrite(img_name, frame)
	# 	print("{} written!".format(img_name))
	# 	img_counter += 1
	#time.sleep(10)
	cam.release()
	#out.release()                      ## for releasing the instance of video saving
	cv2.destroyAllWindows()


if __name__ == '__main__':
	main(img_counter)
