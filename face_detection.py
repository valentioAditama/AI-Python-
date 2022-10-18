import cv2
from isort import stream

# detection 
face_detection = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# default webcam
vid = cv2.VideoCapture(0)

while(True):
    #  capture frae by frame 
    (grabbed, frame) = vid.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # try to detect faces in the webcame 
    faces = face_detection.detectMultiScale(rgb, scaleFactor=1.3, minNeighbors=5)
    # for reach faces found 
    for (x,y,w,h) in faces:
        # Draw a rectangle arounf the face 
        color = (0, 255, 255)
        stroke = 5
        cv2.rectangle(frame, (x,y), (x + w, y + h), color, stroke)
     
    ret, frame = vid.read()

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 

vid.release()
cv2.destroyAllWindows()
cv2.waitKey(1)
cv2.waitKey(1)