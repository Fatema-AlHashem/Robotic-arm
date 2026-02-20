
import cv2

# creating connection to cam
stream=cv2.VideoCapture(0) # 0 is usually the default camera , opens a live video stream


if not stream.isOpened():
    print('not opened!')
    exit()



ret,frame=stream.read() #reads each frame then ret ->boolean (succes or fail) frame->one single frame 
if not ret:
    print("Stream is failing no more frames :( ")
        


    

#display frames as whole 
# cv2.imshow("WebCam",frame) #1st par -> title , 2nd -> frame    


    

stream.release()
cv2.destroyAllWindows()

#as a loop i saw video now not even  apic , just a small pop up then it disaapears 


    








    





