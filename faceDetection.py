import cv2
#make sure you download haarcascade_frontalface_default.xml

facecascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)
cap.set(3,600)
cap.set(4,340)

while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = facecascade.detectMultiScale(imgGray,1.1,4)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(252, 206, 78),2)

    cv2.imshow("original cap",img)
    cv2.imshow("grayscale",imgGray) ## Optional

    if cv2.waitKey(1) & 0xFF == ord('d'):
        break
