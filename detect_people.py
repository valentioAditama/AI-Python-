from re import A
import cv2

video_cap = cv2.VideoCapture('../../../Downloads/people_walking.mp4')
fullbodyCascade = cv2.CascadeClassifier('./Cascade/haarcascade_fullbody.xml')
upperbodyCascade = cv2.CascadeClassifier('./Cascade/haarcascade_upperbody.xml')
lowerbodyCascade = cv2.CascadeClassifier('./Cascade/haarcascade_lowerbody.xml')

video_cap.set(cv2.CAP_PROP_FPS, 120)

while (True):
    ret, img = video_cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    detect_people = fullbodyCascade.detectMultiScale(gray, 1.3, 5)
    lower_body = lowerbodyCascade.detectMultiScale(gray, 1.3, 5)
    upper_body = upperbodyCascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in detect_people:
        cv2.rectangle(img,(x,y), (x+w, y+h), (255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
    
    for (x,y,w,h) in detect_people:
        cv2.rectangle(img,(x,y), (x+w, y+h), (0,255,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
    
    for (x,y,w,h) in detect_people:
        cv2.rectangle(img,(x,y), (x+w, y+h), (0,0,255),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

    cv2.imshow('Preview', img)
    k = cv2.waitKey(30) & 0xff 
    if k == 27:
        break 
    
video_cap.release()
cv2.destroyAllWindows() 
