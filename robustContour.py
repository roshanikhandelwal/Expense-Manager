import cv2
import utlis

def RectangularContour(contours):
    for contour in contours:
        (x,y,w,h) = cv2.boundingRect(contour)
        # cv2.rectangle(imgcopy, (x,y), (x+w,y+h), (0,255,0), 2)
    (x,y,w,h) = utlis.sortedArea(contours)
    # cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
    # img = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_CONSTANT)
    # biggest1, maxArea = utlis.biggestContour1(contours)
    # (x,y,w,h)=biggest1

    # cv2.rectangle(imgcopy, (x,y), (x+w,y+h), (0,0,255), 10)
    # print("error!! biggest",biggest1)
    # img=cv2.resize(img,(heightImg//2,widthImg//2))
    # cv2.imshow("image for try",imgcopy)
    # cv2.waitKey(0)
    # biggest = (x,y,w,h)
    biggest = np.float32([[[x,y],[x+w,y],[x,y+h],[x+w,y+h]]])
    print("x,y,w,h",biggest)
    return biggest
