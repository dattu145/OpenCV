import cv2


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
#wrap perspective
"""
img = cv2.imread('wrap.jpg')

width,height = (250,350)
pts1 = np.float32([[412,133],[653,180],[583,523],[318,465]])
pts2 = np.float32([[0,0],[width,0],[width,height],[0,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
output = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Original image",img)
cv2.imshow("Output Image",output)

cv2.waitKey(0)
"""
#joining 2 or more images into 1 window

"""

img = cv2.imread("580987.jpg")
resize = cv2.resize(img,(200,200))

Horimg = np.hstack((resize,resize))
Verimg = np.vstack((resize,resize))

cv2.imshow("horizontal Image",Horimg)
cv2.imshow("vertical Image",Verimg)
cv2.waitKey(0)

"""
#face detection
""""
facecascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)
cap.set(3,900)
cap.set(4,420)
while True:
    success,img = cap.read()
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = facecascade.detectMultiScale(img,1.1,4)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),1)

    cv2.imshow("original Image",img)
    if cv2.waitKey(1) & 0xFF == ord('w'):
        break

"""
### Displaying fps
"""
import cv2
import time

cap = cv2.VideoCapture(0)
cap.set(3,600)
cap.set(4,340)

fps_start_time = 0
fps = 0

while True:
    success, img = cap.read()

    fps_end_time = time.time()
    time_diff = fps_end_time - fps_start_time
    fps = 1/(time_diff)
    fps_start_time = fps_end_time

    cv2.putText(img,str(int(fps)),(18,340),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,0,0),2)

    cv2.imshow("video Output Original",img)
    if cv2.waitKey(1) & 0xFF == ord('d'):
        break
"""
### hand detection try
"""
import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
cap.set(3,600)
cap.set(4,350)
cap.set(10,100)

mphands = mp.solutions.hands
hands = mphands.Hands()
#later step
mpdraw = mp.solutions.drawing_utils

while True:
    success,img=cap.read()
    ## in hand detection we should convert BGR to RGB
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    result = hands.process(imgRGB)
    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:
            mpdraw.draw_landmarks(img, hand, mphands.HAND_CONNECTIONS)

    cv2.imshow("original output",img)
    if cv2.waitKey(1) & 0xFF == ord('d'):
        break
"""
### colour detection using HSV
"""
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
"""
###qr scanner
"""
import cv2
import numpy as np
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,310)

with open('mydatafile.text') as f:
    myDataList = f.read().split(',')
    print(myDataList)

while True:
    success, img = cap.read()
    code = decode(img)

    for barcode in code:
        myData = barcode.data.decode('utf-8')
        print(myData)

        if myData in myDataList:
            myOutput = 'Authorized'
            myColor = (0,255,0)
        else:
            myOutput = 'Un-Authorized'
            myColor = (0,0,255)

        pts = np.array(barcode.polygon)
        cv2.polylines(img, [pts], True, myColor, 2)
        pts2 = barcode.rect
        cv2.putText(img, myOutput, (pts2[0], pts2[1]-15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, myColor, 2)

    cv2.imshow("original image", img)
    if cv2.waitKey(1) & 0xFF == ord('d'):
        break
"""



















