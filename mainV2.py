import cv2
import numpy as np
import face_recognition
import os
from PIL import Image
import glob
import datetime
import csv

# ---------Instantiating variables-------------
path = 'SavedImages'
impImages = []
ImagesList = []
myImagList = os.listdir(path)
fileName = 'Register.csv'
AccessMode = 'r+'


# --------Upload images to program-------
def uploadImages():
    for image in myImagList:
        currentImage = cv2.imread(f'{path}/{image}')
        impImages.append(currentImage)
        ImagesList.append(os.path.splitext(image)[0])  # Breaks name from format and only specify first element which


# uploadImages() #------------Uploading images


def passRegister(name):
    with open(fileName, AccessMode) as file:
        allRawList = file.readlines()
        regNames = []

        for row in allRawList:
            entry = row.split(',')
            regNames.append(entry[0])

        if name not in regNames:
            currentDate = datetime.datetime.now().strftime('%d-%m-%Y')
            time = datetime.datetime.now().strftime('%H:%M:%S')
            file.writelines(f'{name}, {currentDate} , {time}\n')



# --------Step2:Find encodings-------#
def encodings(ImportedImages):
    global encodedList
    encodedList = []
    for impImag in ImportedImages:
        impImag = cv2.cvtColor(impImag, cv2.COLOR_BGR2RGB)
        encodedImage = face_recognition.face_encodings(impImag)[0]
        encodedList.append(encodedImage)
    return encodedList  # ---method returns the list of encoded images-----


# encodedKnownList = encodings(impImages)
# print("Encoding Completed")
# print(f"There's {len(encodedKnownList)} encodings ")



# -------Step3-1 OPEN AND SET UP WEBCAM------------------
#try:

def startWeb():
    uploadImages()  # ------------Uploading images

    encodedKnownList = encodings(impImages)
    print("Encoding Completed")
    print(f"There's {len(encodedKnownList)} encodings ")

    webcam = cv2.VideoCapture(0)  # ---Initialize webcam
    if not webcam.isOpened():
        raise IOError("Cant open webcam")
    while True:  # Loop to get each frame at a time
        successFrame, imgFrame = webcam.read()  # This provides your image
        imgSmall = cv2.resize(imgFrame, (700, 600), None, 1, 1)  # As we doing this in real time, we need to reduce the size of the image to speed the process
        #imgSmall = cv2.cvtColor(imgSmall, cv2.COLOR_BGR2RGB)
        imgSmall = cv2.flip(imgSmall, 1)

        facesCurrFrame = face_recognition.face_locations(imgSmall)
        encodedCurrFrame = face_recognition.face_encodings(imgSmall, facesCurrFrame)

# ------Step3--2---------FIND MATCHES AND PRINT RESULTS AS WELL AS DISTANCE-------------
        for encodeFace, faceLoc in zip(encodedCurrFrame, facesCurrFrame):
            matches = face_recognition.compare_faces(encodedKnownList, encodeFace)
            faceDistance = face_recognition.face_distance(encodedKnownList, encodeFace)
        #print(faceDistance)
            matchIndex = np.argmin(faceDistance)

            if matches[matchIndex]:
                name = ImagesList[matchIndex].upper()
                y1, x2, y2, x1 = faceLoc




                cv2.rectangle(imgSmall, (x1, y1), (x2, y2), (255, 0, 0), 2)
                cv2.rectangle(imgSmall, (x1, y2-35), (x2, y2), (0, 0, 0), cv2.FILLED)
                cv2.putText(imgSmall, name, (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                passRegister(name)

        cv2.imshow('Input', imgSmall)
        c = cv2.waitKey(1)
        if c == 27:
            print('You pressed Esc to terminate the program')
            cv2.destroyAllWindows()
            break



    webcam.release()
    cv2.destroyAllWindows()


# startWeb()
#except: print("Program terminated")



