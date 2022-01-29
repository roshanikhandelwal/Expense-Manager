from pytesseract import *
from PIL import Image
import cv2
img = cv2.imread("result.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#img=Image.open('file.jpg')
results=pytesseract.image_to_data(img, output_type=Output.DICT)

# Then loop over each of the individual text
# localizations
for i in range(0, len(results["text"])):

    # We can then extract the bounding box coordinates
    # of the text region from  the current result
    x = results["left"][i]
    y = results["top"][i]
    w = results["width"][i]
    h = results["height"][i]

    # We will also extract the OCR text itself along
    # with the confidence of the text localization
    text = results["text"][i]
    conf = int(results["conf"][i])

    # filter out weak confidence text localizations
    if conf:

        # We will display the confidence and text to
        # our terminal
        #print("Confidence: {}".format(conf))
        #print("Text: {}".format(text))
        #print("")

        # We then strip out non-ASCII text so we can
        # draw the text on the image We will be using
        # OpenCV, then draw a bounding box around the
        # text along with the text itself
        text = "".join(text).strip()
        cv2.rectangle(img,
                      (x, y),
                      (x + w, y + h),
                      (0, 0, 255), 2)
        cv2.putText(img,
                    text,
                    (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1.2, (0, 255, 255), 3)

# After all, we will show the output image
cv2.imshow("Image", img)
cv2.waitKey(0)
