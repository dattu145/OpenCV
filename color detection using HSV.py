import cv2
import numpy as np

img = cv2.imread("blue in image.jpg")
resize = cv2.resize(img,(420,300))

imgHSV = cv2.cvtColor(resize, cv2.COLOR_BGR2HSV)


blue_lower = np.array([87,100,50])
blue_upper = np.array([110,255,255])
    # red_lower = np.array([170,100,100])
    # red_upper = np.array([180,255,255])
bluemask = cv2.inRange(imgHSV, blue_lower, blue_upper)
imgBlur = cv2.GaussianBlur(bluemask,(5,5),1)
    # red_mask = cv2.inRange(imgHSV, red_lower, red_upper)
blue = cv2.bitwise_and(resize , resize, mask=imgBlur)
    # red = cv2.bitwise_and(img, img, mask=red_mask)

cv2.imshow("Original image",resize)
cv2.imshow("Original image converted to HSV image",imgHSV)
cv2.imshow("HSV image converted to mask",bluemask)
cv2.imshow("Blur applied to mask",imgBlur)
cv2.imshow("imgBlur to (bitwise_and) color detection",blue)
    # cv2.imshow("red",red)

cv2.waitKey(0)