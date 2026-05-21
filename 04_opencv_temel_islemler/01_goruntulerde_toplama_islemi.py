import cv2
import numpy as np 

# 1. BEYAZ TUVAL ÜZERİNE MAVİ ÇEMBER
# 512x512 boyutlarında, 3 kanallı (BGR) beyaz bir arka plan matrisi oluşturuyoruz.
tuval_cember = np.zeros((512, 512, 3), np.uint8) + 255

# Bu matrisin merkezine (256, 256) 60 piksel yarıçaplı, içi dolu (-1) mavi bir çember çiziyoruz.
cv2.circle(tuval_cember, (256, 256), 60, (255, 0, 0), -1)

# 2. BEYAZ TUVAL ÜZERİNE KIRMIZI KARE
# Aynı boyutlarda ikinci bir beyaz arka plan matrisi oluşturuyoruz.
tuval_kare = np.zeros((512, 512, 3), np.uint8) + 255

# Sol üst (150, 150) ve sağ alt (350, 350) koordinatlarını referans alarak içi dolu kırmızı bir kare çiziyoruz.
cv2.rectangle(tuval_kare, (150, 150), (350, 350), (0, 0, 255), -1)

# 3. GÖRÜNTÜLERİ TOPLAMA (MATRİS TOPLAMASI)
# cv2.add fonksiyonu ile iki farklı matrisi piksel piksel birbiriyle topluyoruz.
# Teknik Not: OpenCV'de toplama işlemi 255 sınırına (satürasyon) tabidir. Toplamı 255'i geçen piksel değerleri 255'e (beyaza) sabitlenir.
tuval_toplam = cv2.add(tuval_cember, tuval_kare)

# Çıktıları pencerelerde görselleştiriyoruz.
cv2.imshow("Mavi Cember Tuvali", tuval_cember)
cv2.imshow("Kirmizi Kare Tuvali", tuval_kare)
cv2.imshow("Iki Matrisin Toplami", tuval_toplam)

# Pencereleri açık tutmak ve bellekten güvenlice silmek için standart bekleme komutlarımız.
cv2.waitKey(0)
cv2.destroyAllWindows()
