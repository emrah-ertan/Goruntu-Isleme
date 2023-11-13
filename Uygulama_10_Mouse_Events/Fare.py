import cv2
import numpy as np

cizim = False
mod = False
xi,yi = -1,-1

def draw(event,x,y,flags,param):
    #print(f"X,Y koordinat : {x,y}")    #Farenin yer aldığı koordinatlar
    global cizim,xi,yi,mod


    if event == cv2.EVENT_LBUTTONDOWN:
        xi,yi = x,y
        cizim = True

    elif event == cv2.EVENT_MOUSEMOVE:
        if cizim ==True:
            if mod==True:
                cv2.circle(img,(x,y),7,(150,0,150),-1)
            else:
                cv2.rectangle(img,(xi,yi),(x,y),(150,0,150),-1)
        else:
            pass

    elif event == cv2.EVENT_LBUTTONUP:
        cizim=False


#cv2 içerisinde event içeren bütün başlıkları görebilmemizi sağlar.
for i in dir(cv2):
    if 'EVENT' in i:
        print(i)

img = np.ones((512,512,3),np.uint8)
cv2.namedWindow("paint")

cv2.setMouseCallback("paint",draw)

while(1):
    cv2.imshow("paint",img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    if cv2.waitKey(1) & 0xFF == ord("m"):
        mod = not mod

cv2.destroyAllWindows()