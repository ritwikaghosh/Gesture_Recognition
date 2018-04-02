import numpy as np
import cv2


def recognise(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_filtered = cv2.GaussianBlur(img_gray, (15, 15), 3)
    _, img_thresh = cv2.threshold(img_filtered, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    img_thresh = cv2.copyMakeBorder(img_thresh, 0, 0, 0, 50, cv2.BORDER_CONSTANT, value=255)
    img_thresh = cv2.GaussianBlur(img_thresh, (25, 25), 5)
    img = cv2.copyMakeBorder(img, 0, 0, 0, 50, cv2.BORDER_REPLICATE)
    _, contours, _ = cv2.findContours(img_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnt = contours[1]
    hull = cv2.convexHull(cnt, returnPoints=True)
    #hull_inv = cv2.convexHull(cnt, returnPoints=False)
    epsilon = 0.02*cv2.arcLength(cnt,True)
    poly = cv2.approxPolyDP(cnt,epsilon,True)
    cv2.drawContours(img, [poly], 0, (0, 255, 0), 3)
    cv2.imshow('Otsu_Result', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# def distance(a, b):
#     return np.linalg.norm(a - b)
