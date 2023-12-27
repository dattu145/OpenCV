import cv2
import numpy as np

# Reading and displaying Images

img = cv2.imread('img1.png')
cv2.imshow("Image Output",img)
cv2.waitKey()


# Reading a Live Stream vide0

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    flipped_img = cv2.flip(img,1) # with horizontal flip orientation
    cv2.imshow("Output",flipped_img)
    if cv2.waitKey(1) & 0xFF == ord('p'):
        break
    
cap.release()
cv2.destroyAllWindows()


# Reading a Video

# Open a video file or capture from a camera (0 for default camera)
cap = cv2.VideoCapture('path/to/video.mp4')

# Check if the video capture object is successfully opened
if not cap.isOpened():
    print("Error: Couldn't open the video.")
    exit()

while True:
    # Read a frame from the video
    ret, frame = cap.read()

    # Check if the frame is successfully read
    if not ret:
        print("Error: Couldn't read a frame.")
        break

    # Display the frame
    cv2.imshow('Video', frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


# Basic Image Operations (Resizing,Cropping,Rotating)

# Resizing :
img = cv2.imread('img1.png')
resized_img = cv2.resize(img,(850,550)) # (width,height)
cv2.imshow("Image Output",resized_img)
cv2.waitKey()

# Cropping :
img = cv2.imread("img1.png")
rows, cols, test = img.shape 
#shape takes 3 parameters height/rows, width/cols ,color channel(bgr = 3,grayscale = 1)
print("Rows :",rows)
print("Cols :",cols)
print("what : ",test)
cv2.rectangle(img,(10,50),(350,310),(0,255,0),1) #img,top-left point,bottom-right point,color,thickness
cropped_img = img[50:310,10:350] # called as ROI (Range of interest)
#img[0:692,0:501] gives us a complete image
cv2.imshow("Output",img)
cv2.imshow("cropped output",cropped_img)
cv2.waitKey(0)

# Rotating :
img = cv2.imread('img1.png')
rotated_img=cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE) #src,rotate_code
cv2.imshow("Output",rotated_img)
cv2.waitKey(0)


## Color spaces

img=cv2.imread('colors.jpg')
grayscale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #blue,green,red to grayscale
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV) #blue,green,red to HSV(Hue,Saturation,Value)
hls = cv2.cvtColor(img,cv2.COLOR_BGR2HLS) #blue,green,red to HLS(Hue,Lightness,Saturation)
cv2.imshow("Original",img)
cv2.imshow("GRAYSCALE",grayscale)
cv2.imshow("HSV",hsv)
cv2.imshow("HLS",hls)
cv2.waitKey(0)


#adding shapes and text to images

img = np.zeros((412,412,3),np.uint8)
#print(img)

img[:] = 8,8,8
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(225,110,0),2)
cv2.rectangle(img,(10,10),(200,110),(0,225,225),2)
cv2.circle(img,(50,300),40,(225,225,225),3)
cv2.putText(img,"Cybertron",(240,190),cv2.FONT_ITALIC,1,(153, 255, 168),1)
cv2.imshow("image",img)
cv2.waitKey(0)
