import cv2
from Recognise import recognise

cap = cv2.VideoCapture(0)

while(True):
    ret, img = cap.read()
    recognise(img)


cap.release()
cv2.destroyAllWindows()