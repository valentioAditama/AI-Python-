import cv2 
import os 

cam = cv2.VideoCapture(0)
face_detection = cv2.CascadeClassifier('./Cascade/haarcascade_frontalface_default.xml')

face_id = input('\n masukan user id = ')
print('Data sedang di process dan siap-siap lihat ke camera, camera akan segera di buka.')

# initialize individual sampling face count 
count = 0
while(True):
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detection.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces: 
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
        count += 1
        # save the captured image into the datasets folder 
        cv2.imwrite("Dataset/user " + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h, x:x+w])

        cv2.imshow('image', img)
    k = cv2.waitKey(100)
    if k == 27:
        break 
    elif count >= 30:
        break 
print("Exitting programs")
cam.release()
cv2.destroyAllWindows()
