import cv2

#img reading

"""
img = cv2.imread('580987.jpg')
width,height = 500,500
imge = cv2.resize(img,(width,height))
print(imge.shape)
cv2.imshow("Resized Output", imge)
cv2.waitKey(5000)
"""

#video reading
"""
cap = cv2.VideoCapture(0)
cap.set(3,840)
cap.set(4,480)
cap.set(10,200)

while True:
    success, img = cap.read()
    #resizedVideo = cv2.resize(img, (width, height))
    cv2.imshow("Resized Output",img)
    if cv2.waitKey(1) & 0xFF == ord('d'):
        break
"""

#changing image Colour(basic functions)
"""
img = cv2.imread('580987.jpg')
resize = cv2.resize(img,(300,300))
Grayscale = cv2.cvtColor(resize,cv2.COLOR_BGR2RGB)
imgBlur = cv2.GaussianBlur(Grayscale,(39,39),0)
imgthreshold = cv2.Canny(resize,100,100)
cv2.imshow("BGR to RGB",Grayscale)
cv2.imshow("Blured img",imgBlur)
cv2.imshow("threshold image",imgthreshold)
cv2.waitKey(0)
"""

#adding shapes and text to images
"""
import numpy as np

img = np.zeros((412,412,3),np.uint8)
#print(img)


img[:] = 8,8,8
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(225,110,0),2)
cv2.rectangle(img,(10,10),(200,110),(0,225,225),2)
cv2.circle(img,(50,300),40,(225,225,225),3)
cv2.putText(img,"Cybertron",(240,190),cv2.FONT_ITALIC,1,(153, 255, 168),1)
cv2.imshow("image",img)
cv2.waitKey(0)
"""