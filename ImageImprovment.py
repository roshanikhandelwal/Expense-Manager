import cv2
import numpy as np


def PerspectiveChanger(biggest,heightImg,widthImg,img):
    print("after reordering",biggest)
    pts1 = np.float32(biggest) # PREPARE POINTS FOR WARP
    print("pts1",pts1)
    # new_wid=biggest[1][0][0]
    # new_hig=biggest[2][0][1]
    # print("a",new_wid,new_hig)
    pts2 = np.float32([[0, 0],[widthImg, 0], [0, heightImg],[widthImg, heightImg]]) # PREPARE POINTS FOR WARP
    print("pts2",pts2)
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgWarpColored = cv2.warpPerspective(img, matrix, (widthImg, heightImg))
    # cv2.imshow("imgWarpColored",imgWarpColored)
    # cv2.waitKey(0)
    # imgWarpColored1 = imgWarpColored[topx:bottomx+1,topy:bottomy+1]
    # cv2.imshow("imgWarpColored1",imgWarpColored1)
    # cv2.waitKey(0)
    # asp_ratio = new_hig/new_wid
    # print("new asp_ratio",asp_ratio)
    #REMOVE 20 PIXELS FORM EACH SIDE #removed-20 as it was cropping too much
    # crop_w=5
    # crop_h=int(asp_ratio*crop_w)
    imgWarpColored=imgWarpColored[10:imgWarpColored.shape[0] , 5:imgWarpColored.shape[1]]
    # imgWarpColored = cv2.resize(imgWarpColored,(new_wid,new_hig))
    # APPLY ADAPTIVE THRESHOLD
    # imgWarpGray = cv2.cvtColor(imgWarpColored,cv2.COLOR_BGR2GRAY)
    imgAdaptiveThre= cv2.adaptiveThreshold(imgWarpColored, 255, 1, 1, 7, 2)
    # imgAdaptiveThre= cv2.adaptiveThreshold(imgWarpGray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
    imgAdaptiveThre = cv2.bitwise_not(imgAdaptiveThre)
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
