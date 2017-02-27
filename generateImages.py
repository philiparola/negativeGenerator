import cv2
import csv
import os

positiveData = csv.reader(open("imagecoords.txt", "r"))
posList = list(positiveData)
negativeData = csv.reader(open("negcoords.txt", "r"))
negList = list(negativeData)

for i in range(0,len(posList)):
    posList[i][1] = int(posList[i][1])
    posList[i][2] = int(posList[i][2])
    posList[i][3] = int(posList[i][3])
    posList[i][4] = int(posList[i][4])

for i in range(0,len(negList)):
    negList[i][1] = int(negList[i][1])
    negList[i][2] = int(negList[i][2])
    negList[i][3] = int(negList[i][3])
    negList[i][4] = int(negList[i][4])

for i in range(0,len(posList)):
    image = cv2.imread(posList[i][0])
    cropped = image[posList[i][3]:posList[i][4], posList[i][1]:posList[i][2]]
    if not os.path.exists("./pos"):
        os.makedirs("./pos")
    fileout = "pos/" + str(i) + ".png"
    cv2.imwrite(fileout, cropped)

for i in range(0,len(negList)):
    image = cv2.imread(negList[i][0])
    cropped = image[negList[i][3]:negList[i][4], negList[i][1]:negList[i][2]]
    if not os.path.exists("./neg"):
        os.makedirs("./neg")
    fileout = "neg/" + str(i) + ".png"
    cv2.imwrite(fileout, cropped)
