import cv2 
import numpy as np 
from PIL import Image 
import os 

# Path for face image database 
path = 'dataset'
recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier('./Cascade/haarcascade_frontalface_default.xml')

# function to get the images and label data 
def getImagesAndLabels(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faceSamples = []
    ids = []
    for imagePath in imagePaths:
        PIL_img = Image.open(imagePath).convert('L') # Grayscale 
        img_numpy = np.array(PIL_img, 'uing8')
        id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces = detector.detectMultiScale(img_numpy)
        for (x,y,w,h) in faces:
            faceSamples.append(img_numpy[y:y+h, x:x+w])
            ids.append(id)
    return faceSamples,ids

print("\n Training faces. akan segera di mulai....")

faces.ids = getImagesAndLabels(path)
recognizer.train(faces, np.array(ids))

# Save the model into trainer/trainer.yml 
recognizer.write('trainer/trainer.yml')

# Print the number of faces trainer and end program 
print('faces trained. exiting')
Program.format(len(np.unique(ids)))