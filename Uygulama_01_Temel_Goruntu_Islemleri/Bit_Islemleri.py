import cv2
import numpy as np
from matplotlib import pyplot as plt


def logo_yerlestir(path_1,path_2):
    path_1 = "./" + path_1
    path_2= "./"+path_2

    image_1 = cv2.imread(path_1)
    image_2 = cv2.imread(path_2)

    x,y,z = image_1.shape
    roi = image_2[0:x,0:y]          #image_2 gorüntüsünün belirtilen kısmı kırpıldı


    image_1_gray = cv2.cvtColor(image_1,cv2.COLOR_BGR2GRAY)

    ret, image_1_gray_thresh = cv2.threshold(image_1_gray,10,255,cv2.THRESH_BINARY)

    cv2.imshow("Original",image_1)
    cv2.imshow("Gray",image_1_gray)
    cv2.imshow("2. Original",image_2)
    cv2.imshow("Thresh (mask)",image_1_gray_thresh)
    cv2.imshow("Cropped (roi)",roi)

    image_1_gray_thresh_inv = cv2.bitwise_not(image_1_gray_thresh)

    cv2.imshow("Thresh Invert",image_1_gray_thresh_inv)

    image_1_bg  = cv2.bitwise_and(roi,roi,mask=image_1_gray_thresh_inv)
    image_2_fg = cv2.bitwise_and(image_1,image_1,mask=image_1_gray_thresh)
    cv2.imshow("Image_1 BG",image_1_bg)
    cv2.imshow("Image_2 FG",image_2_fg)

    toplam = cv2.add(image_1_bg,image_2_fg)

    cv2.imshow("Toplam",toplam)

    image_2[0:x,0:y] = toplam

    cv2.namedWindow("Result",cv2.WINDOW_NORMAL)
    cv2.imshow("Result",image_2)


    cv2.waitKey(0)
    cv2.destroyAllWindows()