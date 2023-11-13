import cv2
import numpy as np

def goster(path):
    path = "./" + path

    image  = cv2.imread(path)
    hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

    lower_blue = np.array([90, 50, 50])        # Parametreler sırasıyla H - S - V değerlerini temsil etmektedir.
    upper_blue = np.array([130, 255, 255])      # Girilen aralık mavi rengi tespit etmek için kullanılmaktadır.

    mask  = cv2.inRange(hsv,lower_blue,upper_blue)
    result = cv2.bitwise_and(image,image,mask=mask)



    cv2.imshow("Orijinal Göl",image)
    #cv2.imshow("HSV Göl",hsv)
    cv2.imshow("Mask",mask)
    cv2.imshow("Sonuç",result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()