
import cv2

# creating connection to cam
stream=cv2.VideoCapture(0) # 0 is usually the default camera , opens a live video stream


if not stream.isOpened():
    print('not opened!')
    exit()


while(True):
    ret,frame=stream.read() #reads each frame , returns the frame and boolean
    if not ret:
        print("Stream is failing no more frames :( ")
        break


    #display frames as whole 
    cv2.imshow("WebCam",frame) #1st par -> title , 2nd -> frame


    # To exit from webcam , we can use if we click somthing we can exit from stream 
    # waitKey(time in ms) --> means wait so open CV can update and to listen to keyboard
    if cv2.waitKey(1)== ord('q'): # Not sure abt roboArm tho ?
        break   

stream.release()
cv2.destroyAllWindows()




    








    





