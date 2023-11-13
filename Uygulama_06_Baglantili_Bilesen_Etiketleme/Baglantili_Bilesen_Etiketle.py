import cv2
import numpy as np


def etiketle(path):
    path = "./"+path


    image_gray = cv2.imread(path,0)
    _,image_thresh = cv2.threshold(image_gray,140,255,cv2.THRESH_BINARY)

    # Bağlantılı bileşen etiketleme yap
    num_labels, labels = cv2.connectedComponents(image_thresh)

    # İlk etiketi arkaplan olarak kabul et (genellikle en büyük etikettir)
    num_objects = num_labels - 1

    # Sonuçları göster
    print(f"Görüntüdeki nesne sayısı: {num_objects}")

    # Nesneleri farklı renklerle işaretle
    colored_labels = np.zeros((image_gray.shape[0], image_gray.shape[1], 3), dtype=np.uint8)
    for label in range(1, num_labels):
        colored_labels[labels == label] = np.random.randint(0, 255, size=3)
    cv2.imshow("Labeled Objects", colored_labels)
    cv2.waitKey(0)
    cv2.destroyAllWindows()