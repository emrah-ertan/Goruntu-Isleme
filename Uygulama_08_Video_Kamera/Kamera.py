import cv2
import numpy as np


def Kamera_Anlik_Goruntu_Al():
    cam = cv2.VideoCapture(0)
    while cam.isOpened():
        ret, frame = cam.read()

        cv2.imshow("Kamera Goruntusu",frame)

        if(cv2.waitKey(1) & 0xFF  == ord("q")):
            break


    cam.release()
    cv2.destroyAllWindows()


def Kamera_Goruntu_Kaydet():
    cam = cv2.VideoCapture(0)
    fourrc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter("VideoGoruntu.avi",fourrc,30.0,(640,480))     #Parametreler sırasıyla: isim, değişken, fps, boyutlar şeklinde

    while cam.isOpened():
        ret, frame = cam.read()
        out.write(frame)
        cv2.imshow("kamera",frame)

        if cv2.waitKey(1) == ord("q"):
            break

    cam.release()
    out.release()
    cv2.destroyAllWindows()