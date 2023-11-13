import os
import cv2
import numpy as np
from matplotlib import pyplot as plt


def tum_resimleri_goruntule(directory_path):
    dosya_isimleri = []

    # Klasördeki dosyaları listele
    for dosya in os.listdir(directory_path):
        # Dosya adını listeye ekleyin
        dosya_isimleri.append(dosya)

    # Dosya isimlerini içeren listeyi yazdır
    print(dosya_isimleri)

    for i in dosya_isimleri:
        image = cv2.imread("./" + directory_path + "/" + i)
        cv2.imshow("image", image)
        cv2.waitKey(0)



def piksel_topla(pixel_1,pixel_2):


    piksel_1 = np.uint8([pixel_1])
    piksel_2 = np.uint8([pixel_2])
    piksel_toplam = cv2.add(piksel_1,piksel_2)
    print(piksel_toplam)


def goruntu_topla(path_1,path_2):
    path_1 = "./" + path_1
    path_2 = "./" + path_2
    image_1 = cv2.imread(path_1)
    image_2 = cv2.imread(path_2)


    image_toplam = cv2.addWeighted(image_1,0.7,image_2,0.3,0) #ilk resim, ilk resmin ağırlığı, ikinci resim, ikinci resmin ağırlığı, gamma(parlaklık) değeri
    #ağırlıksız toplama için cv2.add(image_1,image_2)

    cv2.imshow("1. Image",image_1)
    cv2.imshow("2. Image", image_2)
    cv2.imshow("Last Image", image_toplam)


    cv2.waitKey(0)
    cv2.destroyAllWindows()



def kirp(path):
    path = "./" + path
    image = cv2.imread(path)
    cropped_image = image[100:300,100:300]

    #Kırpılan kısmı orjinal görüntüye yerleştirme
    #image[400:600,400:600] = cropped_image

    plt.subplots(121)
    plt.imshow(image)
    plt.subplot(122)
    plt.imshow(cropped_image)
    plt.show()


    cv2.waitKey(0)
    cv2.destroyAllWindows()