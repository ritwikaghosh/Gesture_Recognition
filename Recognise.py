import numpy as np
import cv2
f=open("onoff.txt","w")

def recognise(img):
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    img_gray = img_hsv[:,:,1]
    img_filtered = cv2.GaussianBlur(img_gray, (25, 25), 5)
    _, img_thresh = cv2.threshold(img_filtered, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    img_thresh = cv2.copyMakeBorder(img_thresh, 0, 0, 0, 50, cv2.BORDER_CONSTANT, value=255)
    kernel = np.ones((8, 8), np.uint8)
    img_thresh = cv2.dilate(img_thresh,kernel,iterations = 1)#cv2.GaussianBlur(img_thresh, (25, 25), 5)
    img = cv2.copyMakeBorder(img, 0, 0, 50, 50, cv2.BORDER_REPLICATE)
    _, contours, _ = cv2.findContours(img_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnt = contours[0]
    hull = cv2.convexHull(cnt, returnPoints=True)
    #hull_inv = cv2.convexHull(cnt, returnPoints=False)
    epsilon = 0.02*cv2.arcLength(cnt,True)
    poly = cv2.approxPolyDP(cnt,epsilon,True)
    flag = len(poly)
    print(flag)
    if(flag<=8):
        f.write("0")
        #insert logic for off
    else:
        f.write("1")
        #insert logic for on



    cv2.drawContours(img, [poly], 0, (0, 255, 0), 3)
    #cv2.imshow('Otsu_Result', img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()


# def distance(a, b):
#     return np.linalg.norm(a - b)


def explore(img):
    img_hsv  = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    img_h = img_hsv[:,:,1];
    _, img_thresh = cv2.threshold(img_h, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    kernel = np.ones((15,15), np.uint8)
    img_thresh = cv2.dilate(img_thresh, kernel, iterations=1)  # cv2.GaussianBlur(img_thresh, (25, 25), 5)
    cv2.imshow('Image',img_thresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
