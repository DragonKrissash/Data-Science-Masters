import cv2
import dlib
import numpy as np
#capture image

cap = cv2.VideoCapture(0)


#recognise face

face_det = dlib.get_frontal_face_detector()

# Logic

while True :
  
  ret,frame = cap.read()                          #Read & Capture the frame of image
  frame = cv2.flip(frame , 1)                     #Vertically flip the image

  #Greyscaling the image

  grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  faces = face_det(hrey)

  # To make rectangle around image and to put no. on it

  i=0
  for face in faces :

    # Faces kaa co-ordinates

    x,y = face.left() , face.top()
    x1,y1 = face.right() , face.bottom()

    # Rectangle

    cv2.rectangle(frame(x,y),frame(x1,y1),(0,255,0),2)

    #Writing Text

    i=i+1
    cv2.putText(frame , "Face num ",str(i),(x-10,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)

  cv2.imshow('frame' , frame)

  # Loop ke baahar aane ke liye code
  # Code to out from the loop

  if(cv2.waitKey(1) & 0xFF == ord('q')):
    break
cap.release()
cv2.destroyAllWindows()
\

