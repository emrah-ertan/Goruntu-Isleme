import cv2
import numpy as np
from matplotlib import pyplot as plt

def cizgi_ciz():
    img_matrix = np.zeros((512, 512,3), np.uint8)

    cv2.imshow("Arkaplan Goruntu", img_matrix)
    cv2.line(img_matrix, (0, 0), (511, 511), (0, 255, 0),7)  #Sırasıyla parametreler: görüntü, çizgi başlangıcı, çizgi bitişi, çizgi rengi, çizgi kalınlığı

    cv2.imshow("Cizgi",img_matrix)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def dikdortgen_ciz():
    img_matrix = np.zeros((512,512,3),np.uint8)

    cv2.imshow("Arkaplan Goruntu",img_matrix)
    cv2.rectangle(img_matrix,(30,30),(70,70),(255,0,0),5) #Sırasıyla parametreler: görüntü, dikdörtgen başlangıcı, dikdörtgen bitişi, dikdörtgen rengi, dikdörtgen kalınlığı
    cv2.rectangle(img_matrix,(75,75),(120,120),(0,255,0),-1) #Kalınlık parametresi -1 ise dikdörtgenin içi doldurulur

    cv2.imshow("Son Goruntu",img_matrix)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def cember_ve_daire_ciz():
    img_matrix = np.zeros((512, 512, 3), np.uint8)
    cv2.imshow("Arkaplan Goruntu", img_matrix)
    cv2.circle(img_matrix,(255,255),60,(50,75,120),2) #Sırasıyla parametreler: görüntü, çember merkezi, yarıçap, renk, kalınlık
    cv2.circle(img_matrix, (70, 120), 60, (50, 75, 120),-1)  #Kalınlık -1 girilirse çember yerine daire olur

    cv2.imshow("Son Goruntu",img_matrix)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def elips_ciz():
    img_matrix = np.zeros((512, 512, 3), np.uint8)
    cv2.imshow("Arkaplan Goruntu", img_matrix)

    cv2.ellipse(img_matrix,(256,256),(100,50),0,0,180,(255,255,255),3)
    cv2.ellipse(img_matrix, (100, 100), (50, 50), 0, 0, 180, (255, 255, 255), -1)

    cv2.imshow("Son Goruntu", img_matrix)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def cokgen_ciz():
    img_matrix = np.zeros((512, 512, 3), np.uint8)
    cv2.imshow("Arkaplan Goruntu", img_matrix)

    noktalar = np.array([[20,30],[170,120],[255,255],[10,400]])
    noktalar_list = noktalar.reshape(-1,1,2)
    cv2.polylines(img_matrix,[noktalar_list],True,(255,255,255),3)

    cv2.imshow("Son Goruntu", img_matrix)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def yazi_yaz():
    img_matrix = np.zeros((512, 512, 3), np.uint8)
    cv2.imshow("Arkaplan Goruntu", img_matrix)

    font= cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(img_matrix,"OpenCV ile Yazı Yazdırma",(10,250),font,4,(0,0,255),2,cv2.LINE_AA)

    cv2.imshow("Son Goruntu", img_matrix)

    cv2.waitKey(0)
    cv2.destroyAllWindows()