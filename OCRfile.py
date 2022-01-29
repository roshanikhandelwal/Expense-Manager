import cv2
from pytesseract import *


def InfoExtractor(imgAdaptiveThre,filename):
    results=pytesseract.image_to_data(imgAdaptiveThre, output_type=Output.DICT)
    extracted_text=pytesseract.image_to_string(imgAdaptiveThre)
    # Then loop over each of the individual text
    # localizations
    for i in range(0, len(results["text"])):
        # extract the bounding box coordinates of the text region from
        # the current result
        x = results["left"][i]
        y = results["top"][i]
        w = results["width"][i]
        h = results["height"][i]
        # extract the OCR text itself along with the confidence of the
        # text localization
        text = results["text"][i]
        conf = int(results["conf"][i])
        if conf > 20:
            # strip out non-ASCII text so we can draw the text on the image
            # using OpenCV, then draw a bounding box around the text along
            # with the text itself
            text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
            cv2.rectangle(imgAdaptiveThre, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(imgAdaptiveThre, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,1, (200, 0 ,0), 3)
            cv2.imwrite("sample-images/processed-image/Image-Info-Extracted.jpg", imgAdaptiveThre)
    file = open(filename,"w")
    file.writelines(extracted_text)
    file.close()
    return imgAdaptiveThre
