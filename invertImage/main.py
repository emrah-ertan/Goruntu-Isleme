import cv2
import numpy as np
from matplotlib import pyplot as plt

foto = cv2.imread("parrot.jpg",0)

cv2.imshow("Papagan",foto)

maxDeger = np.max(foto)
satir,sutun = np.shape(foto)

for i in range(satir):
    for j in range(sutun):
        foto[i,j]  = maxDeger - foto[i,j]

cv2.imshow("Papagan Tersi",foto)

cv2.waitKey()