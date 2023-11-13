import cv2
import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans


def k_means_bolutle(path):
    path = "./"+path
    image = cv2.imread(path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Görüntüyü yeniden boyutlandır (isteğe bağlı)
    # image = cv2.resize(image, (new_width, new_height))

    # Görüntüyü düz bir matrise dönüştür
    pixels = image.reshape((-1, 3))

    # K-Means modelini oluştur ve uygula
    num_clusters = 5  # Bölütlenmek istenen küme sayısı
    kmeans = KMeans(n_clusters=num_clusters,n_init='auto')
    kmeans.fit(pixels)

    # Her pikseli en yakın kümesine atayarak görüntüyü yeniden şekillendir
    segmented_image = kmeans.cluster_centers_[kmeans.labels_]
    segmented_image = segmented_image.astype(np.uint8)
    segmented_image = segmented_image.reshape(image.shape)

    # Orjinal ve bölütlenmiş görüntüleri göster
    cv2.imshow("Original Image", image)
    cv2.imshow("Segmented Image", segmented_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def watershed_bolutle(path):
    path = "./" + path
    image = cv2.imread(path)
    image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    # Morfolojik işlemlerle arka planı temizleme
    kernel = np.ones((3, 3), np.uint8)
    opening = cv2.morphologyEx(image_gray, cv2.MORPH_OPEN, kernel, iterations=2)

    # Sure background area
    sure_bg = cv2.dilate(opening, kernel, iterations=3)

    # Morfolojik işlemlerle nesne alanını tespit etme
    dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
    ret, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)

    # Arka plan ve nesne bölgelerini birleştirme
    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg, sure_fg)

    # Nesne bölgelerini etiketleme
    ret, markers = cv2.connectedComponents(sure_fg)

    # Etiketlenmiş bölgeleri artırma
    markers = markers + 1
    markers[unknown == 255] = 0

    # Watershed algoritmasını uygulama
    markers = cv2.watershed(image, markers)
    image[markers == -1] = [0, 0, 255]  # Sınırları kırmızı renkte işaretle

    # Sonuçları göster
    plt.subplot(121), plt.imshow(image, cmap='gray')
    plt.title('Görüntü'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(markers, cmap='jet')
    plt.title('Nesne Etiketleri'), plt.xticks([]), plt.yticks([])
    plt.show()



    cv2.waitKey(0)
    cv2.destroyAllWindows()