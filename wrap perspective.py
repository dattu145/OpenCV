import cv2

img = cv2.imread('wrap.jpg')

width,height = (250,350)
pts1 = np.float32([[412,133],[653,180],[583,523],[318,465]])
pts2 = np.float32([[0,0],[width,0],[width,height],[0,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
output = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Original image",img)
cv2.imshow("Output Image",output)

cv2.waitKey(0)