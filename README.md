# Expense-Manager
## GETTING STARTED
to run this on your own machine:
- Start by creating a virtual env if you have anaconda : ```conda create -n envname python==3.6.8 pip```
- Setup a new virtual environment and install the depencencies from the **requirements.txt** file ```pip install -r requirements.txt```
- Clone this repository
- Run **main.py** on the saved images in *sample-image* directory by using the following code in the terminal ``` python main.py --image path-to-image ```
- Hope it was useful!!

## STEPS PERFORMED:
1. The **main.py** file drives the entire program.
2. Skew correction is performed to check for skewness/rotation in the bill if found it is corrected.
3. Performing canny-edge detection with dilation and erosion to normalize the text and finding there respective boundaries.
4. Finding all the contoury present.
5. Looking for the biggest contour of them all which will indeed be required and further used.
6. Changing the perspective(warping) according to the biggest contour which will be tthe focus area and enhancing the image
7. Optical Character Recognition is later performed on the transformed image.
8. From the extacted text from the previous step we apply Named Entity Recognition using **spacy**.

## RESULTS:

### Sample-Image
- ![Sample-Image](https://github.com/parikshit14/exp-manager/blob/master/sample-images/receipt-scanned.jpg)

### Image-After-thresholding
- ![Image-After-thresholding](https://github.com/parikshit14/exp-manager/blob/master/sample-images/processed-image/Image-After-thresholding.jpg)

### Image-After-SkewCorrection
- ![Image-After-SkewCorrection](https://github.com/parikshit14/exp-manager/blob/master/sample-images/processed-image/Image-After-SkewCorrection.jpg)

### Image-After-ContourDetection
- ![Image-After-ContourDetection](https://github.com/parikshit14/exp-manager/blob/master/sample-images/processed-image/Image-After-ContourDetection.jpg)

### Image-After-CannyEdgeDetection
- ![Image-After-CannyEdgeDetection](https://github.com/parikshit14/exp-manager/blob/master/sample-images/processed-image/Image-After-CannyEdgeDetection.jpg)

### Image-After-ChangingPerception
- ![Image-After-ChangingPerception](https://github.com/parikshit14/exp-manager/blob/master/sample-images/processed-image/Image-After-ChangingPerception.jpg)

### Image-Info-Extracted
- ![Image-Info-Extracted](https://github.com/parikshit14/exp-manager/blob/master/sample-images/processed-image/Image-Info-Extracted.jpg)
