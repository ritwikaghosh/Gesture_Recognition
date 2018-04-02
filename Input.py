import cv2
from Recognise import recognise
from Recognise import explore

img = cv2.imread("sample images/Open 1.jpg")
recognise(img)
#explore(img)