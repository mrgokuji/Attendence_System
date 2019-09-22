import cv2,os
#from grey_video import STD_DIMENSIONS

def detect_faces(f_cascade, color_img, scaleFactor=1.1):
	img_copy = color_img.copy()

	gray = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)

	faces = f_cascade.detectMultiScale(gray, scaleFactor = scaleFactor)#minNeighbors=10)
	path = '/root/Documents/miniProject/ML Part/facial_recogn/test_cropped'
	#img_counter = 1

	for (x,y,w,h) in faces:
		#cv2.rectangle(img_copy, (x,y), (x+w,y+h), (0,255,0), 2)
#################################################################
		crop_img = img_copy[y:y+h, x:x+w]
		img_counter = len(os.listdir(os.path.join(os.getcwd(),'test_cropped')))
		img_name = "{}.png".format(img_counter)
		cv2.imwrite(os.path.join(path , img_name), crop_img)
		#cv2.imshow("cropped", crop_img)
		#cv2.waitKey(0)
	return img_copy


haar_file = cv2.CascadeClassifier('data/haarcascade_frontalface_alt.xml')

def main(img_counter,file):
	#files = os.listdir(os.path.join(os.getcwd(),'test', str(img_counter) + '.png'))
	# file = os.path.join(os.getcwd(),'test', str(img_counter) + '.png')
	print(file)
	test_img = cv2.imread(file)
	test_img = detect_faces(haar_file,test_img)
	'''
	for file in files:
		test_img = cv2.imread('test/'+file)
		i = img_counter
		test_img = detect_faces(haar_file,test_img,i)

		#cv2.imshow(file,test_img)
		#cv2.waitKey(0)
		cv2.destroyAllWindows()

	'''
if __name__ == '__main__':
	main(img_counter)
