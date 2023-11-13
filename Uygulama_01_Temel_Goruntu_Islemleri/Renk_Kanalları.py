import cv2
import numpy as np
from matplotlib import pyplot as plt

def show_bgr_channels(path):
    path = "./"+path
    image = cv2.imread(path)

    # Resmi kanallara bölme
    b, g, r = cv2.split(image)
    print(f"b : {b}")
    print(f"g : {g}")
    print(f"r : {r}")
    # Kanalları tekrar birleştirme
    image_2 = cv2.merge((b, g, r))

    #Kanalları ayırmanın 2. yolu
    B = image[:,:,0]
    G = image[:,:,1]
    R = image[:,:,2]

    cv2.imshow("B (Blue) Channel",B)
    cv2.imshow("G (Green) Channel",G)
    cv2.imshow("R (Red) Channel",R)




    cv2.waitKey(0)
    cv2.destroyAllWindows()



def bgr_gray_donustur(path):
    path = "./"+path

    image = cv2.imread(path)
    image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    cv2.imshow("Gray Image",image_gray)

    cv2.waitKey(0)
    cv2.destroyAllWindows()



def bgr_hsv_donustur(path):
    path = "./" + path

    image = cv2.imread(path)
    image_hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

    cv2.imshow("HSV Image",image_hsv)


    cv2.waitKey(0)
    cv2.destroyAllWindows()


def renkli_nesne_tespiti(path):
    path = "./" + path
    image = cv2.imread(path)
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([110,50,50])           #110-130 cv2 için hsv uzayında mavi rengin değeridir
    upper_blue = np.array([130,255,255])         #110-130 cv2 için hsv uzayında mavi rengin değeridir
    #lower_green = np.array([50, 50, 50])  # 50-70 cv2 için hsv uzayında yeşil rengin değeridir
    #upper_green = np.array([70, 255, 255])  # 50-70 cv2 için hsv uzayında yeşil rengin değeridir

    mask = cv2.inRange(image_hsv, lower_blue, upper_blue)
    res = cv2.bitwise_and(image, image, mask=mask)  # bitsel 'and' işlemi

    cv2.imshow("Image Result", res)
    cv2.imshow("Image Mask",mask)
    cv2.imshow("Image HSV", image_hsv)
    cv2.imshow("Image Original", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def canlı_renkli_nesne_tespiti():

    cam  = cv2.VideoCapture(0)

    while cam.isOpened():
        _,frame = cam.read()
        frame_hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

        lower_blue = np.array([110,50,50])           #110-130 cv2 için hsv uzayında mavi rengin değeridir
        upper_blue = np.array([130,255,255])         #110-130 cv2 için hsv uzayında mavi rengin değeridir
        lower_green = np.array([50,50,50])           #50-70 cv2 için hsv uzayında yeşil rengin değeridir
        upper_green = np.array([70,255,255])         #50-70 cv2 için hsv uzayında yeşil rengin değeridir

        mask = cv2.inRange(frame_hsv,lower_blue,upper_blue)
        res = cv2.bitwise_and(frame,frame,mask=mask)    #bitsel 'and' işlemi


        cv2.imshow("Original (BGR)",frame)
        cv2.imshow("HSV",frame_hsv)
        cv2.imshow("Mask",mask)
        cv2.imshow("Bitwise And",res)

        if(cv2.waitKey(1) & 0xFF == ord("q")):
            break

    cv2.destroyAllWindows()