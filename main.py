import face_detection
import time
import model
import cv2
import os
import imageReciever
from datetime import datetime

Server_time = ['09:00','10:00','11:15','12:15','13:15','15:00','16:00','16:34']


img_counter = 0
try:
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        time.sleep(5)
        print(current_time)
        if  current_time in Server_time:         # ESC pressed    k%256 == 27 or
            print("Server time started")
            imageReciever.main()
            break





    # while True:
    #     ret, frame = cam.read()
    #     img_name = "{}.png".format(img_counter)
    #     path = os.getcwd()+'/test/'
    #     cv2.imwrite(os.path.join(path , img_name), frame)
    #     print("{} written!".format(img_name))
    #     img_counter += 1
    #     #k = cv2.waitKey(1)
    #     #time.sleep(2)
    #     if  img_counter > 10:         # ESC pressed    k%256 == 27 or
    #         print("Escape hit, closing...")
    #        break
except Exception as e:
    print("Error in recoding the video\nDue to following error : ")
    print(e)


file = os.path.join(os.getcwd(),'test', str(img_counter) + '.png')
try:
    while(img_counter<=10):
        face_detection.main(img_counter,file)
        img_counter+=1
        file = os.path.join(os.getcwd(),'test', str(img_counter) + '.png')


except Exception as e:
    print("Error in detection of faces\nDue to following error : ")
    print(e)
    # try:
    #     model.main()
    # except Exception as e:
    #     print("Error in recoding the video\nDue to following error : ")
    #     print(e)
# cam.release()
# cv2.destroyAllWindows()
# time.sleep(1)


database = os.listdir(os.path.join(os.getcwd(),'database'))
data = os.path.join(os.getcwd(),'database')
test_cropped = os.listdir(os.path.join(os.getcwd(),'test_cropped'))
test = os.path.join(os.getcwd(),'test_cropped')

present_imgs = set()
for img1 in database:
     for img2 in test_cropped:
        # print (,'       ',img2)
          if model.main(str(data) +'/'+ str(img1),str(test) +'/'+ str(img2)):
              present_imgs.add(img1)
              break
print(present_imgs)
