import cv2
import os
from datetime import datetime
import socket
import sys
import time

cam = cv2.VideoCapture(0)

#function to click an image and saving as 1.png,2.png,etc.....
def click_pic(img_counter):
	ret, frame = cam.read()
	img_name = "{}.png".format(img_counter)
	path = '/home/pi/attendence/'
	cv2.imwrite(os.path.join(path , img_name), frame)
	print("{} written!".format(img_name))


break_time = ['09:00','10:00','11:15','12:15','13:15','15:00','16:00','02:59']

img_counter = 0

while True:
	now = datetime.now()
	current_time = now.strftime("%H:%M")

	click_pic(img_counter)

	img_counter += 1
	#k = cv2.waitKey(1)
	time.sleep(5)
	print(current_time)
	if  current_time in break_time:         # ESC pressed    k%256 == 27 or
		print("Escape hit, closing...")
		break


##################################################################################################

files = os.listdir('/home/pi/attendence/')


host = '192.168.43.195'
port = 5000



image = '/home/pi/attendence/'
for file in files:
	s = socket.socket() #socket creation
	s.connect((host,port)) #establishinng connection 
	f = open(image + file,'rb') #opening the file in read mode
	l = f.read(1024)
	while (l):
		s.send(l)	#sending the file 
		l = f.read(1024)
	s.close()
