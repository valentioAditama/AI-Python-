import numpy as np 
import cv2 

faceCascade = cv2.CascadeClassifier('./Cascade/haarcascade_frontalface_default.xml')
eyesCascade = cv2.CascadeClassifier('./Cascade/haarcascade_eye.xml')
cap = cv2.VideoCapture(0)

while (True):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray, 
        scaleFactor=1.3,
        minNeighbors=5, 
        minSize=(20, 20)
    )

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y), (x+w, y+h), (225,122,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        eyes = eyesCascade.detectMultiScale(
        roi_gray,
        scaleFactor=1.5,
        minNeighbors=5, 
        minSize=(5, 5)
        
        )

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0,255, 0), 2)

    cv2.imshow('video', img)

    k = cv2.waitKey(30) & 0xff 
    if k == 27: 
        break 

cap.release()
cv2.destroyAllWindows()