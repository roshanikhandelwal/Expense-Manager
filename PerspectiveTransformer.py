import cv2
import numpy as np


def PerspectiveChanger(biggest,heightImg,widthImg,img):
    # print("after reordering",biggest)
    pts1 = np.float32(biggest) # PREPARE POINTS FOR WARP
    # print("pts1",pts1)
    pts2 = np.float32([[0, 0],[widthImg, 0], [0, heightImg],[widthImg, heightImg]]) # PREPARE POINTS FOR WARP
    # print("pts2",pts2)
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgWarpColored = cv2.warpPerspective(img, matrix, (widthImg, heightImg))
    imgWarpColored=imgWarpColored[10:imgWarpColored.shape[0] , 5:imgWarpColored.shape[1]]
    imgAdaptiveThre= cv2.adaptiveThreshold(imgWarpColored, 255, 1, 1, 7, 2)
    imgAdaptiveThre = cv2.bitwise_not(imgAdaptiveThre)
    cv2.imshow("perspective",imgAdaptiveThre)
    cv2.waitKey(0);
    cv2.imwrite("sample-images/processed-image/Image-After-ChangingPerception.jpg", imgAdaptiveThre)
    kernel = np.array([[0, -1, 0],
                      [-1, 5,-1],
                      [0, -1, 0]])

    # Sharpen image
    image_sharp = cv2.filter2D(imgAdaptiveThre, -1, kernel)
    # image_sharp = cv2.fastNlMeansDenoisingMulti(image_sharp, 2, 1, None, 4, 7, 35)
    cv2.imshow("sharp",image_sharp)
    cv2.waitKey(0)
    imgAdaptiveThre=cv2.medianBlur(image_sharp,3)
    return imgAdaptiveThre
