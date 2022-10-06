import cv2
import winsound
import imghdr
import time
import smtplib
import pyautogui
import pygetwindow
from email.message import EmailMessage
from PIL import Image

time.sleep(2)
cap = cv2.VideoCapture(0)

width = 600
height = 310

cap.set(3,width)
cap.set(4,height)
cap.set(10,50)

fps_start = 0
fps = 0

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to


    with open("result.png", 'rb') as f:
        time.sleep(1)
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name

    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename="thiefs.jpg")

    user = "daddyphone145233@gmail.com"
    msg['from'] = user
    passwd = "dkmymwirgissmqqy"


    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, passwd)
    server.send_message(msg)

    server.quit()

def scrshot(path):
    # path = r"C:\Users\Dell\PycharmProjects\filehandling\result.png"
    titles = pygetwindow.getAllTitles()

    window = pygetwindow.getWindowsWithTitle("Original Output")[0]
    left, top = window.topleft
    right, bottom = window.bottomright

    pyautogui.screenshot(path)
    im = Image.open(path)
    im = im.crop((left + 10, top + 10, right - 10, bottom - 10))
    im.save(path)


while True:
    success, img1 = cap.read()
    success, img2 = cap.read()
    diff = cv2.absdiff(img1, img2)

    fps_end = time.time()
    time_diff = fps_end - fps_start
    fps = 1/(time_diff)
    fps_start = fps_end

    cv2.putText(img1,"fps : " + str(int(fps)),(width-550,height+140),cv2.FONT_HERSHEY_SIMPLEX,1.1,(0,255,0),2)

    grayscale = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grayscale,(5,5),0)
    _, threshold = cv2.threshold(grayscale,20,255,cv2.THRESH_BINARY)
    dilated = cv2.dilate(threshold, None, iterations=1)
    contours, _ = cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        if cv2.contourArea(c) > 20000:
            x, y, w, h = cv2.boundingRect(c)
            # cv2.rectangle(img1, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.drawContours(img1, contours, -1, (0, 255, 0), 2)
            print("thief detected")
            if __name__ == '__main__':
                scrshot(r"C:\Users\Dell\PycharmProjects\filehandling\result.png")
            winsound.PlaySound("error beep sound.wav",winsound.SND_ASYNC)
            email_alert("Security Alert","Person detected(Code Red)","sridharreddy145233@gmail.com")

    cv2.imshow("Original Output",img1)

    if cv2.waitKey(1) & 0xFF == ord('d'):
        break
