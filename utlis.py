import cv2
import numpy as np
import math

def reorder(myPoints):
    flag=0
    s_of_myPoints = myPoints.size//2
    if s_of_myPoints == 4:
        myPoints = myPoints.reshape((4, 2))
        myPointsNew = np.zeros((4, 1, 2), dtype=np.int32)
        add = myPoints.sum(1)
        # print("add",add)
        myPointsNew[0] = myPoints[np.argmin(add)]
        myPointsNew[3] =myPoints[np.argmax(add)]
        diff = np.diff(myPoints, axis=1)
        myPointsNew[1] =myPoints[np.argmin(diff)]
        myPointsNew[2] = myPoints[np.argmax(diff)]
        # print("myPointsNew",myPointsNew)
    else:
        flag=1
        myPointsNew=0
    return myPointsNew,flag


def biggestContour(contours):
    biggest = np.array([])
    max_area = 0
    for i in contours:
        area = cv2.contourArea(i)
        if area > 5000:
            peri = cv2.arcLength(i, True)
            approx = cv2.approxPolyDP(i, 0.02 * peri, True)
            if area > max_area and len(approx) >=4 and len(approx) <=6:
                biggest = approx
                max_area = area
    # print("biggest",biggest)
    return biggest,max_area

def biggestContour1(contours):
    biggest = np.array([])
    max_area = 0
    for i in contours:
        area = cv2.contourArea(i)
        if area > 5000:
            approx = cv2.boundingRect(i)
            # peri = cv2.arcLength(i, True)
            # approx = cv2.approxPolyDP(i, 0.02 * peri, True)
            if area > max_area :
                biggest = approx
                max_area = area
    return biggest,max_area

def sortedArea(contours):
    area = []
    coordinates = []
    for i in contours:
      # print("i:",i)
      (x,y,w,h) = cv2.boundingRect(i)
      # print("w,h",w,h)
      areas = w*h
      if areas > 5000:
        coordinates.append(cv2.boundingRect(i))
        area.append(areas)
    area.sort()
    # print("area",area)
    # print("coordinates",coordinates)
    wanted_area = math.floor(area[-2])
    # print("wanted_area",wanted_area)
    for x,y,w,h in coordinates:
        # print("x,y,w,h",x,y,w,h)
        areas =  math.floor(w*h)
        # print("area:",areas)
        if areas == wanted_area:
            req_coordinates = (x,y,w,h)
    # print(area)
    # print(req_coordinates)
    return req_coordinates

def nothing(x):
    pass

def initializeTrackbars(intialTracbarVals=0):
    cv2.namedWindow("Trackbars")
    cv2.resizeWindow("Trackbars", 360, 240)
    cv2.createTrackbar("Threshold1", "Trackbars", 200,255, nothing)
    cv2.createTrackbar("Threshold2", "Trackbars", 200, 255, nothing)


def valTrackbars():
    Threshold1 = cv2.getTrackbarPos("Threshold1", "Trackbars")
    Threshold2 = cv2.getTrackbarPos("Threshold2", "Trackbars")
    src = Threshold1,Threshold2
    return src
