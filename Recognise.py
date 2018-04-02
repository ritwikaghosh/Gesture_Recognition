import numpy as np
import cv2

def recognise(img):
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img_filtered = cv2.GaussianBlur(img_gray,10)
    _,img_thresh = cv2.threshold(img_filtered,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    cv2.imshow('Otsu_Result',img_thresh)