img = cv2.imread("580987.jpg")
resize = cv2.resize(img,(200,200))

Horimg = np.hstack((resize,resize))
Verimg = np.vstack((resize,resize))

cv2.imshow("horizontal Image",Horimg)
cv2.imshow("vertical Image",Verimg)
cv2.waitKey(0)