# Predefined libraries
import cv2
import numpy as np
##############
import utlis
import argparse
import SkewCorrection
import CannyErosionDilation
import ContourDetector
import RobustContour
import PerspectiveTransformer
import OCRfile
import NERfile
###############

# Taking image path as an argument
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image to be scanned")
args = vars(ap.parse_args())
outfilename='mytxt.txt'

image = cv2.imread(args['image'])
heightImg,widthImg = image.shape[:2]
asp_ratio=float(heightImg)/float(widthImg)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)
cv2.waitKey(0)

# Correcting skew
img = SkewCorrection.skewCorrector(gray,heightImg,widthImg)

# Canney edge detection and dilation
imgThreshold = CannyErosionDilation.CannyErosionDilation(img)

# FIND ALL COUNTOURS
contours = ContourDetector.FindingContour(image,imgThreshold)

biggest, maxArea = utlis.biggestContour(contours) # FIND THE BIGGEST CONTOUR
if biggest.size != 0:
    biggest,flag=utlis.reorder(biggest)
    #handling exception
    if flag == 1:  # If the contour Has more than 4 coordinates( in case of incomplete image or an edge is folded)
        biggest = RobustContour.RectangularContour(contours)
    # Changing the perspective of the image
    imgAdaptiveThre = PerspectiveTransformer.PerspectiveChanger(biggest,heightImg,widthImg,img)


cv2.imshow("best_one",imgAdaptiveThre)
cv2.waitKey(0)
cv2.imwrite("sample-images/processed-image/Image-After-Sharpening.jpg", imgAdaptiveThre)

# Applying OCR on the processed image
image_after_ocr = OCRfile.InfoExtractor(imgAdaptiveThre,outfilename)
cv2.imshow("Image", image_after_ocr)
cv2.waitKey(0)

# Named Entity Recogniion on the extracted data
bill_date,bill_total,bill_organisation = NERfile.InfoSpecifier(outfilename)
print(bill_date,bill_total,bill_organisation)
