import cv2
import numpy
import csv
import random

positiveData = csv.reader(open("imagecoords.txt", "r"))

posList = list(positiveData)
negList = [None] * len(posList)
for i in range(0,len(negList)):
    negList[i] = [None] * 5

for i in range(0,len(posList)):
    posList[i][1] = int(posList[i][1])
    posList[i][2] = int(posList[i][2])
    posList[i][3] = int(posList[i][3])
    posList[i][4] = int(posList[i][4])

#Append image dimensions
for i in range(0, len(posList)):
    img = cv2.imread(posList[i][0])
    posList[i].append(numpy.size(img, 0)) #height
    posList[i].append(numpy.size(img, 1)) #width

#[filename, upper left x, lower right x, upper left y, lower right y,]
for i in range(0, len(posList)):
    negList[i][0] = posList[i][0]
    widthBoundingBox = posList[i][2] - posList[i][1]
    heightBoundingBox = posList[i][4] - posList[i][3]

    widthNegBox = widthBoundingBox
    heightNegBox = heightBoundingBox
    #aspect ratio between 2:3 and 3:2, fix this later

    overlapFound = True
    while overlapFound is True:
        overlapFound = False
        negList[i][3] = random.randint(0,posList[i][5]-heightNegBox)
        negList[i][1] = random.randint(0,posList[i][6]-widthNegBox)

        negList[i][4] = negList[i][3] + heightNegBox
        negList[i][2] = negList[i][1] + widthNegBox

        for j in range(0, len(posList)):
            if not (negList[i][1] > posList[j][2] or negList[i][3] > posList[j][4] or negList[i][2] < posList[j][1] or negList[i][4] < posList[j][2]):
                overlapFound = True

        for k in range(0, len(negList)):
            if not (negList[i][1] > posList[k][2] or negList[i][3] > posList[k][4] or negList[i][2] < posList[k][1] or negList[i][4] < posList[k][2]):
                overlapFound = True

negativeData = csv.writer(open("negcoords.txt", "w", newline=''))

for i in range(0, len(negList)):
    negativeData.writerow(negList[i])
