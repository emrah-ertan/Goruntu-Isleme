import cv2
import numpy as np

def erosion(path):
    path = "./"+path
    image_gray = cv2.imread(path,0)

    _, image_thresh= cv2.threshold(image_gray,120,255,cv2.THRESH_BINARY)
    kernel = np.ones((5,5),np.uint8)
    image_erode = cv2.erode(image_thresh,kernel,iterations=1)
    cv2.imshow("Image Erode",image_erode)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def dilation(path):
    path = "./" + path
    image_gray = cv2.imread(path, 0)

    _, image_thresh = cv2.threshold(image_gray, 120, 255, cv2.THRESH_BINARY)
    kernel = np.ones((5, 5), np.uint8)
    image_dilate = cv2.dilate(image_thresh, kernel, iterations=1)
    cv2.imshow("Image Dilate", image_dilate)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

#Gradient işlemi genişleme - erozyon işlemidir. Manuel olarak yapılabildiği gibi morphologyEx kullanılarak da yapılabilir
def gradient(path):
    path = "./" + path
    image_gray = cv2.imread(path, 0)

    _, image_thresh = cv2.threshold(image_gray, 120, 255, cv2.THRESH_BINARY)
    kernel = np.ones((5, 5), np.uint8)
    image_erode = cv2.erode(image_thresh, kernel, iterations=1)
    image_dilate = cv2.dilate(image_thresh,kernel,iterations=1)
    image_gradient = image_dilate-image_erode
    image_gradient_with_morphologyEx = cv2.morphologyEx(image_thresh,cv2.MORPH_GRADIENT,kernel)

    cv2.imshow("Image Gradient", image_gradient)
    cv2.imshow("Image Gradient with morphologyEx",image_gradient_with_morphologyEx)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


#Açma işlemi = erozyon + genişleme işlemlerinin sırayla uygulanmasıdır. Manuel yapılabileceği gibi morphologyEx kullanılarak da yapılabilir
def opening(path):
    path="./"+path
    image_gray = cv2.imread(path, 0)

    _, image_thresh = cv2.threshold(image_gray, 120, 255, cv2.THRESH_BINARY)
    kernel = np.ones((5, 5), np.uint8)

    opening = cv2.morphologyEx(image_thresh, cv2.MORPH_OPEN, kernel)

    cv2.imshow("Opening Image",opening)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

#Kapatma işlemi = genişleme + erozyon işlemlerinin sırayla uygulanmasıdır. Manuel olarak yapılabileceği gibi morphologyEx kullanılarak da yapılabilir
def closing(path):
    path = "./" + path
    image_gray = cv2.imread(path, 0)

    _, image_thresh = cv2.threshold(image_gray, 120, 255, cv2.THRESH_BINARY)
    kernel = np.ones((5, 5), np.uint8)

    closing = cv2.morphologyEx(image_thresh, cv2.MORPH_CLOSE, kernel)
    cv2.imshow("Closing Image", closing)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


#Üst Şapka dönüşümü okunan görüntüden, görüntünün açılma işlemi sonucunun çıkarılması ile elde edilir. T = Image - Opening_Image
def ust_sapka_donusumu(path):
    path = "./" + path
    image_gray = cv2.imread(path, 0)

    kernel = np.ones((5,5),np.uint8)
    image_ust_sapka = image_gray - cv2.morphologyEx(image_gray,cv2.MORPH_OPEN,kernel)


    cv2.imshow("T Hat Image",image_ust_sapka)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#Alt Şapka dönüşümü okunan görüntüye uygulanan kapatma işlemin sonucundan okunan görüntünün çıakrılmasıyla elde edilir. B = Closing_Image - Image
def alt_sapka_donusumu(path):
    path = "./" + path
    image_gray = cv2.imread(path, 0)

    kernel = np.ones((5, 5), np.uint8)
    #image_alt_sapka = cv2.morphologyEx(image_gray, cv2.MORPH_CLOSE, kernel) -image_gray
    image_alt_sapka = image_gray -cv2.morphologyEx(image_gray, cv2.MORPH_CLOSE, kernel)

    cv2.imshow("B Hat Image", image_alt_sapka)
    cv2.waitKey(0)
    cv2.destroyAllWindows()