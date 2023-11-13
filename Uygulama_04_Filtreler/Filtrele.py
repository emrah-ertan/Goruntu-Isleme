import cv2
import numpy as np
import random

def ortalama_filtre(path):
    path = "./"+path
    image_gray = cv2.imread(path,0)

    image_blur_with_cv2 = cv2.blur(src=image_gray,ksize=(5,5))


    blur_filter1 = np.ones((3, 3)) / (9.0)
    blur_filter2 = np.ones((8, 8)) / (64.0)
    blur_filter3 = np.ones((10, 10)) / (100.0)
    image_blur1 = cv2.filter2D(image_gray, -1, blur_filter1)
    image_blur2 = cv2.filter2D(image_gray, -1, blur_filter2)
    image_blur3 = cv2.filter2D(image_gray, -1, blur_filter3)

    cv2.imshow('Gri Görüntü', image_gray)
    cv2.imshow('Image Blur With cv2',image_blur_with_cv2)
    cv2.imshow('Image Blur 1', image_blur1)
    cv2.imshow('Image Blur 2', image_blur2)
    cv2.imshow('Image Blur 3', image_blur3)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def gaussian_median_filtre(path):
    path="./"+path
    image=cv2.imread(path)
    gaussian_blur = cv2.GaussianBlur(image, (5, 5), 0) #diğer parametrelerin pek etkisi yok
    median_blur = cv2.medianBlur(image, 5)
    cv2.imshow('Original Image', image)
    cv2.imshow('Gaussian Blur', gaussian_blur)
    cv2.imshow('Median Blur', median_blur)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def gaussian_gurultu_ekle(path):
    path="./"+path
    image = cv2.imread(path)
    # gri veya renkli olarak okutulursa shape[2] kaldırılır ya da eklenir
    gauss = np.random.normal(0, 1, image.size)
    gauss =gauss.reshape(image.shape[0], image.shape[1], image.shape[2]).astype('uint8')
    # Görüntüye gaussian gürültü ekleme
    img_gauss = cv2.add(image, gauss)
    cv2.imshow('Gauss Gurultu', gauss)
    cv2.imshow('Gurultulu Goruntu',img_gauss)
    # Speckle gürültü ekleme
    # speckle_noise = image + image * gauss


    cv2.waitKey(0)
    cv2.destroyAllWindows()


def tuz_biber_gurultu_ekle(path):
    path="./"+path
    image_gray=cv2.imread(path,0)
    row, col = image_gray.shape
    # 5000 ve 10000 arasında bir sayı üretme
    number_of_pixels = random.randint(5000, 10000)
    for i in range(number_of_pixels):
        # rastgele Y koordinatı belirleme
        y_coord = random.randint(0, row - 1)
        # rastgele X koordinatı belirleme
        x_coord = random.randint(0, col - 1)
        # belirlenen koordinatı beyaz yapma
        image_gray[y_coord][x_coord] = 255
    # 5000 ve 10000 arasında bir sayı üretme
    number_of_pixels = random.randint(5000, 10000)
    for i in range(number_of_pixels):
        # rastgele Y koordinatı belirleme
        y_coord = random.randint(0, row - 1)
        # rastgele X koordinatı belirleme
        x_coord = random.randint(0, col - 1)
        # belirlenen koordinatı siyah yapma
        image_gray[y_coord][x_coord] = 0

    cv2.imshow('Image', image_gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def periyodik_gurultu_ekle(path):
    path="./"+path
    image_gray = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    sh = image_gray.shape[0], image_gray.shape[1]
    noise = np.zeros(sh, dtype='float64')
    X, Y = np.meshgrid(range(0, sh[1]), range(0, sh[0]))
    A = 40
    u0 = 45
    v0 = 50
    noise += A * np.sin(X * u0 + Y * v0)
    A = -18
    u0 = -45
    v0 = 50
    noise += A * np.sin(X * u0 + Y * v0)
    noiseada = image_gray + noise
    gaussian_blur = cv2.GaussianBlur(noiseada, (3, 3), 0)
    cv2.imshow('Image Gray', image_gray)
    cv2.imshow('Gaussian Blur', gaussian_blur)
    cv2.imshow('Image Noise', noiseada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def canny_kenar_algila(path):
    path="./"+path

    image_gray = cv2.imread(path,0)
    image_canny_edges = cv2.Canny(image_gray, threshold1=100, threshold2=200)   #Eşik değerler görüntüye göre ayarlanır

    cv2.imshow("Canny Edges", image_canny_edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def laplacian_kenar_algila(path):
    path="./"+path

    image_gray=cv2.imread(path,0)
    image_laplacian_edges = cv2.Laplacian(image_gray, cv2.CV_64F)

    cv2.imshow("Laplacian Edges",image_laplacian_edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def sobel_kenar_algila(path):
    path="./"+path

    image_gray=cv2.imread(path,0)

    sobel_x = cv2.Sobel(image_gray, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(image_gray, cv2.CV_64F, 0, 1, ksize=3)
    image_sobel_edges = cv2.magnitude(sobel_x, sobel_y)


    cv2.imshow("Sobel Edges", image_sobel_edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def scharr_kenar_algila(path):
    path = "./" + path

    image_gray = cv2.imread(path, 0)

    scharr_x = cv2.Scharr(image_gray, cv2.CV_64F, 1, 0)
    scharr_y = cv2.Scharr(image_gray, cv2.CV_64F, 0, 1)
    image_scharr_edges = cv2.magnitude(scharr_x, scharr_y)

    cv2.imshow("Scharr Edges", image_scharr_edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()