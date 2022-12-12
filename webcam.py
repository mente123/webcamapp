from cgitb import reset
from tkinter import Frame
from unittest import result
import cv2

imgcapture = cv2.VideoCapture(0) # connecting the webcam of the pc using it's id (0)

result = True

while(result):
    ret, frame = imgcapture.read()  
    cv2.imwrite('img.jpg', frame)
    result = False
    print('Image is captured')
    
imgcapture.release()