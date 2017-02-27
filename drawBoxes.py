import cv2
import csv

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

img = cv2.imread('2488.png')

for i in range(0, len(posList)):
    cv2.line(img, (posList[i][1], posList[i][3]), (posList[i][2], posList[i][3]), (0,255,0))
    cv2.line(img, (posList[i][1], posList[i][4]), (posList[i][2], posList[i][4]), (0,255,0))
    cv2.line(img, (posList[i][1], posList[i][3]), (posList[i][1], posList[i][4]), (0,255,0))
    cv2.line(img, (posList[i][2], posList[i][3]), (posList[i][2], posList[i][4]), (0,255,0))

for i in range(0, len(negList)):
    cv2.line(img, (negList[i][1], negList[i][3]), (negList[i][2], negList[i][3]), (0,0,255))
    cv2.line(img, (negList[i][1], negList[i][4]), (negList[i][2], negList[i][4]), (0,0,255))
    cv2.line(img, (negList[i][1], negList[i][3]), (negList[i][1], negList[i][4]), (0,0,255))
    cv2.line(img, (negList[i][2], negList[i][3]), (negList[i][2], negList[i][4]), (0,0,255))

cv2.imshow("Behold",img)
cv2.waitKey()
