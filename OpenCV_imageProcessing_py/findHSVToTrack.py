import cv2
import numpy as np

flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print (flags)

#BGR --> Gray and BGR --> HSV
blue = np.uint8([[[ 255,255,255 ]]])
green = np.uint8([[[ 0,255,0 ]]])
red = np.uint8([[[ 0,0,255 ]]])
hsv_blue = cv2.cvtColor(blue,cv2.COLOR_BGR2HSV)

print('Convert HSV for blue', hsv_blue)
hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
print('Convert HSV for green', hsv_green)
hsv_red = cv2.cvtColor(red,cv2.COLOR_BGR2HSV)
print('Convert HSV for red', hsv_red)