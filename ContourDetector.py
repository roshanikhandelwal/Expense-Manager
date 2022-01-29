import cv2

## FIND ALL COUNTOURS
def FindingContour(img,imgThreshold):
    imgContours = img.copy() # COPY IMAGE FOR DISPLAY PURPOSES
    # imgBigContour = img.copy() # COPY IMAGE FOR DISPLAY PURPOSES
    _, contours,_ = cv2.findContours(imgThreshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # FIND ALL CONTOURS
    cv2.drawContours(imgContours, contours, -1, (0, 255, 0), 2) # DRAW ALL DETECTED CONTOURS
    # resized=cv2.resize(imgContours,(heightImg//2,widthImg//2))
    cv2.imshow("contoured image",imgContours)
    cv2.waitKey(0)
    cv2.imwrite("sample-images/processed-image/Image-After-ContourDetection.jpg", imgContours)
    return contours
