import cv2
import numpy as np 

# 1. BEYAZ TUVAL ÜZERİNE MAVİ ÇEMBER ÇİZİMİM
# İlk olarak 512x512 boyutlarında, 3 kanallı (BGR) tamamen beyaz bir arka plan matrisi oluşturuyorum.
tuval_cember = np.zeros((512, 512, 3), np.uint8) + 255

# Bu tuvalin tam merkezine (256, 256) 60 piksel yarıçapında, içi dolu (-1) mavi bir çember yerleştiriyorum.
cv2.circle(tuval_cember, (256, 256), 60, (255, 0, 0), -1)


# 2. BEYAZ TUVAL ÜZERİNE KIRMIZI KARE ÇİZİMİM
# Aynı boyutlarda, kareyi çizeceğim ikinci beyaz arka plan matrisimi hazırlıyorum.
tuval_kare = np.zeros((512, 512, 3), np.uint8) + 255

# Belirlediğim (150, 150) ve (350, 350) koordinatları arasına içi dolu kırmızı bir kare çiziyorum.
cv2.rectangle(tuval_kare, (150, 150), (350, 350), (0, 0, 255), -1)


# 3. AĞIRLIKLI TOPLAMA (ALPHA BLENDING) İŞLEMİM
# İşte asıl olay burada. cv2.addWeighted ile iki matrisi birleştiriyorum. 
# Mavi çembere %70 (0.7), kırmızı kareye %30 (0.3) saydamlık ağırlığı veriyorum. 
# Ekstra parlaklık (gamma) istemediğim için son parametreyi 0 olarak geçiyorum.
agirlikli = cv2.addWeighted(tuval_cember, 0.7, tuval_kare, 0.3, 0)


# Çıktıları pencerelerde görselleştirerek kendi yazdığım alpha blending sonucunu inceliyorum.
cv2.imshow("Mavi Cember Tuvali", tuval_cember)
cv2.imshow("Kirmizi Kare Tuvali", tuval_kare)
cv2.imshow("Agirlikli Degelerin Goruntusu", agirlikli)


# Son olarak pencerelerin ekranda kalmasını sağlayıp, tuşa basıldığında belleği güvenlice temizliyorum.
cv2.waitKey(0)
cv2.destroyAllWindows()
