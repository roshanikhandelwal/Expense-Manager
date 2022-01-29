import cv2
import numpy as np
import utlis

def RectangularContour(contours):
    for contour in contours:
        (x,y,w,h) = cv2.boundingRect(contour)
    (x,y,w,h) = utlis.sortedArea(contours)
    biggest = np.float32([[[x,y],[x+w,y],[x,y+h],[x+w,y+h]]])
    # print("x,y,w,h",biggest)
    return biggest
