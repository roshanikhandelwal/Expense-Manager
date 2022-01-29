import cv2
import numpy as np
#1)BLURING 2)CANNY-EDGE-DETECTION(DETECTS MAIN OBJECTS AND TURN OTHERS BLACK)
#3)DIALATING- CLEANING OR DILUTING
#4)ERODING- THINING
def CannyErosionDilation(img):
    imgBlur = cv2.GaussianBlur(img, (5, 5), 1) # ADD GAUSSIAN BLUR
    # thres=utlis.valTrackbars() # GET TRACK BAR VALUES FOR THRESHOLDS
    imgThreshold = cv2.Canny(imgBlur,10,50) # APPLY CANNY BLUR( provides options to change the threshold values)
    cv2.imshow("canny image",imgThreshold)
    cv2.waitKey(0)
    cv2.imwrite("sample-images/processed-image/Image-After-CannyEdgeDetection.jpg", imgThreshold)
    kernel = np.ones((5,5))
    imgDial = cv2.dilate(imgThreshold, kernel, iterations=2)
    cv2.imshow("eroded",imgDial)
    cv2.waitKey(0)
    imgThreshold = cv2.erode(imgDial, kernel, iterations=1)
    cv2.imshow("dilated",imgThreshold)
    cv2.waitKey(0)
    return imgThreshold
