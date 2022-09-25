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