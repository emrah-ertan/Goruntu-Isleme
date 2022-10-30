import cv2
import numpy as np
from matplotlib import pyplot as plt


papagan = cv2.imread("parrot.jpg")
cv2.imshow("papagan",papagan)

B = papagan[:,:,0]
G = papagan[:,:,1]
R = papagan[:,:,2]


print("Papağan shape: ",papagan.shape) #yükseklik, genişlik ve kanal sayısı
satirSayisi,sutunSayisi,kanalSayisi = papagan.shape
print("Satır Sayısı: ",satirSayisi)
print("Sütun Sayısı: ",sutunSayisi)
print("Kanal Sayısı: ",kanalSayisi)


## Histogram Oluşturma
print("-----------------------")
print("HiSTOGRAM OLUSTURMA")

#papaganGray = 0.2989 * R + 0.5870 * G + 0.1140 * B
papaganGray  = cv2.imread("parrot.jpg",0)
#print(papaganGray)

histogramArray = list()
for i in range(256):
    histogramArray.append(0)

for i  in range(satirSayisi):
    for j in range(sutunSayisi):
        yogunlukDegeri = papaganGray[i,j]
        histogramArray[yogunlukDegeri] +=1

print(histogramArray)

plt.plot(range(256),histogramArray)
plt.show()


cv2.waitKey()