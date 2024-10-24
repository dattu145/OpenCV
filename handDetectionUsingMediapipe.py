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
