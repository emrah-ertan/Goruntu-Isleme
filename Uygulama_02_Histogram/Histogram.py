import cv2
from matplotlib import pyplot as plt


def show_histogram(path):
    path = "./" + path
    image_gray  = cv2.imread(path,0)

    histogram = cv2.calcHist([image_gray], [0], None, [256], [0, 256])
    plt.figure("Image Gray Histogram")
    plt.title("Gri Görüntü Histogramı")
    plt.plot(histogram)
    plt.show()

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def equalize(path):
    path= "./"+path
    image_gray = cv2.imread(path,0)
    cv2.imshow("Original Image",image_gray)
    histogram_image = cv2.calcHist([image_gray],[0],None,[256],[0,256])
    plt.figure("Gray Image Histogram")
    plt.title("Gray Image Histogram")
    plt.plot(histogram_image)
    plt.show()

    image_equalized = cv2.equalizeHist(image_gray)
    cv2.imshow("Equalized Image",image_equalized)
    histogram_image_equalized = cv2.calcHist([image_equalized], [0], None, [256], [0, 256])
    plt.figure("Equalized Image Histogram")
    plt.title("Equalized Image Histogram")
    plt.plot(histogram_image_equalized)
    plt.show()

    cv2.waitKey(0)
    cv2.destroyAllWindows()