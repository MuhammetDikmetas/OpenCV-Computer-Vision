import cv2
import numpy as np 

# Trackbar oluştururken OpenCV'nin zorunlu istediği boş bir fonksiyon tanımlıyoruz.
def bos_fonksiyonumuz(x):
    pass

# 512x512 boyutlarında, 3 kanallı (BGR) siyah bir pencere matrisi oluşturuyoruz.
pencerem = np.zeros((512, 512, 3), dtype=np.uint8)

# Oluşturduğumuz pencereye bir ad veriyoruz.
# Bunun amacı, trackbar'lar ile görüntülenecek pencerenin aynı isim altında eşleşmesini sağlamak.
cv2.namedWindow("Benim_pencerem")

# Şimdi trackbar'larımızı (kızaklarımızı) oluşturuyoruz.
# Parametreler sırasıyla: Trackbar adı, yerleşeceği pencere adı, başlangıç değeri, bitiş değeri ve çalışacak fonksiyon.
cv2.createTrackbar("R", "Benim_pencerem", 0, 255, bos_fonksiyonumuz)
cv2.createTrackbar("G", "Benim_pencerem", 0, 255, bos_fonksiyonumuz)
cv2.createTrackbar("B", "Benim_pencerem", 0, 255, bos_fonksiyonumuz)

# Uygulamayı tamamen açıp kapatabilmek için bir switch (anahtar) yapısı kuruyoruz.
switch = "0: OFF, 1: ON"
cv2.createTrackbar(switch, "Benim_pencerem", 0, 1, bos_fonksiyonumuz)

# Kızakların konumlarını anlık olarak takip edebilmek için dinamik bir döngü başlatıyoruz.
while True:
    # Güncellenen renk değerleriyle birlikte penceremizi ekranda gösteriyoruz.
    cv2.imshow("Benim_pencerem", pencerem)
    
    # Klavyeden 'q' tuşuna basıldığında döngüden çıkılmasını sağlıyoruz.
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
        
    # Kızakların o anki konum değerlerini tek tek değişkenlerimize aktarıyoruz.
    r = cv2.getTrackbarPos("R", "Benim_pencerem")
    g = cv2.getTrackbarPos("G", "Benim_pencerem")
    b = cv2.getTrackbarPos("B", "Benim_pencerem")
    s = cv2.getTrackbarPos(switch, "Benim_pencerem")
    
    # Eğer anahtar '0' (OFF) konumundaysa pencereyi tamamen siyah yapıyoruz.
    if s == 0:
        pencerem[:] = [0, 0, 0]
        
    # Eğer anahtar '1' (ON) konumundaysa kızaklardan gelen BGR değerlerini matrise atıyoruz.
    if s == 1:
        pencerem[:] = [b, g, r]

# Döngü bittiğinde tüm pencereleri güvenli bir şekilde kapatıyoruz.
cv2.destroyAllWindows()
