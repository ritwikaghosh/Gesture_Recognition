import numpy as np
import cv2

def recognise(img):
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img_filtered = cv2.GaussianBlur(img_gray,(15,15),3)
    _,img_thresh = cv2.threshold(img_filtered,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    _, contours,  _ = cv2.findContours(img_thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cnt = contours[0]
    cv2.drawContours(img,[cnt],0,(0,255,0),3)
    cv2.imshow('Otsu_Result',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()