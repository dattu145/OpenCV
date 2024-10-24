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
