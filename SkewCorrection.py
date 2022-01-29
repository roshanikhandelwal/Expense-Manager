import cv2
import numpy as np

def skewCorrector(gray,heightImg,widthImg):
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    cv2.imshow("thresh",thresh)
    cv2.waitKey(0)
    cv2.imwrite("sample-images/processed-image/Image-After-thresholding.jpg", thresh)
    coords = np.column_stack(np.where(thresh > 0))
    angle = cv2.minAreaRect(coords)[-1]
    # the `cv2.minAreaRect` function returns values in the
    # range [-90, 0); as the rectangle rotates clockwise the
    # returned angle trends to 0 -- in this special case we
    # need to add 90 degrees to the angle
    if angle < -45:
        angle = -(90 + angle)
    # otherwise, just take the inverse of the angle to make
    # it positive
    else:
        angle = -angle
    # rotate the image to deskew it
    center = (widthImg // 2, heightImg // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    img = cv2.warpAffine(gray, M, (widthImg, heightImg), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    cv2.imshow("rotated image",img)
    cv2.waitKey(0)
    cv2.imwrite("sample-images/processed-image/Image-After-SkewCorrection.jpg", img)
    return img
