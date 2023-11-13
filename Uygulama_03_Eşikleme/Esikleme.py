import cv2

def esikle(path,esik_degeri,maksimum_yogunluk_degeri=255):
    path = "./"+path
    image = cv2.imread(path)
    image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    _, image_binary = cv2.threshold(image_gray,esik_degeri,maksimum_yogunluk_degeri,cv2.THRESH_BINARY)
    _, image_binary_inv= cv2.threshold(image_gray,esik_degeri,maksimum_yogunluk_degeri,cv2.THRESH_BINARY_INV)
    _, image_trunc = cv2.threshold(image_gray, esik_degeri,maksimum_yogunluk_degeri, cv2.THRESH_TRUNC)
    _, image_tozero = cv2.threshold(image_gray, esik_degeri,maksimum_yogunluk_degeri, cv2.THRESH_TOZERO)
    _, image_tozero_inv = cv2.threshold(image_gray, esik_degeri,maksimum_yogunluk_degeri, cv2.THRESH_TOZERO_INV)

    cv2.imshow('Gray Image',image_gray)
    cv2.imshow('Binary Threshold', image_binary)
    cv2.imshow('Binary Threshold Inverted', image_binary_inv)
    cv2.imshow('Truncated Threshold', image_trunc)
    cv2.imshow('Set to 0', image_tozero)
    cv2.imshow('Set to 0 Inverted', image_tozero_inv)
    cv2.waitKey(0)
    cv2.destroyAllWindows()