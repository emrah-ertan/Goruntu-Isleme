import cv2
import numpy as np


click_count = 0
a = []

def draw(event,x,y,flags,param):
    #print(x,y)     #Mouse koordinatları x,y ile alınıyor
    global click_count,a

    if click_count <4:
        if event == cv2.EVENT_LBUTTONDBLCLK:
            click_count+=1
            a.append((x,y))
    else:
        src_points = np.float32([
            [a[0][0],a[0][1]],
            [a[1][0],a[1][1]],
            [a[2][0],a[2][1]],
            [a[3][0],a[3][1]]])

        dst_points = np.float32([
            [0,0],
            [cols-1,0],
            [0,rows-1],
            [cols-1,rows-1]])

        click_count = 0
        a = []

        M= cv2.getPerspectiveTransform(src_points,dst_points)
        image_output = cv2.warpPerspective(image,M,(cols,rows))

        cv2.namedWindow("Output",cv2.WINDOW_NORMAL)
        cv2.imshow("Output",image_output)




def paperScanner(path):
    path = "./"+path
    global image,rows,cols
    image = cv2.imread(path)


    rows,cols = image.shape[:2]


    cv2.namedWindow("Image",cv2.WINDOW_NORMAL)

    cv2.setMouseCallback("Image",draw)

    while(1):
        cv2.imshow("Image",image)

        if(cv2.waitKey(1) & 0xFF == ord("q")):
            break
    cv2.destroyAllWindows()