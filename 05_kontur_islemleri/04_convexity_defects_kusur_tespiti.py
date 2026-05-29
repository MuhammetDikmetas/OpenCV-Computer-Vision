import cv2
import numpy as np


data_path = "C:\\Users\\muham\\Desktop\\goruntu_isleme\\kodlar\\veri\\yildiz.jpg"

img = cv2.imread(data_path)


img = cv2.resize(img, (640, 480))

# Kontur algoritmaları için görüntümü BGR uzayından Gri (Grayscale) tona indirgiyorum.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Arka planı siyah, hedef nesneyi (yıldızı) beyaz yapmak için ters (INV) binary eşikleme uyguluyorum.
ret, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)

# Siyah-beyaz maske üzerindeki tüm sınırları (konturları) tespit ediyorum.
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Görüntüdeki olası gürültüleri eleyip, sadece en büyük alana sahip ana konturu (yıldızın kendisini) seçiyorum.
cnt = max(contours, key=cv2.contourArea)

# Kusurları (defects) bulabilmek için Convex Hull fonksiyonunun koordinatları değil, indeksleri döndürmesini (returnPoints=False) sağlıyorum.
hull = cv2.convexHull(cnt, returnPoints=False)

# Nesnenin dışbükey örtüsü (hull) ile kendi sınırları arasında kalan içe çökük bölgeleri (kusurları) hesaplıyorum.
defects = cv2.convexityDefects(cnt, hull)

# Döngünün çökmesini engellemek için, matematiksel olarak bir kusur matrisi dönüp dönmediğini kontrol ediyorum.
if defects is not None:
    
    # Bulduğum tüm kusur (çukur) noktaları üzerinde dönüyorum.
    for i in range(defects.shape[0]):
        # Başlangıç (s), bitiş (e), en derin nokta (f) indekslerini ve bu noktanın dış örtüye olan mesafesini (d) çekiyorum.
        s, e, f, d = defects[i, 0]
        
        # Ufak pürüzleri filtrelemek ve sadece gerçekten derin oyukları (yıldızın iç köşelerini) yakalamak için mesafe sınırı koyuyorum.
        if d > 1000:
            # İndeksleri kullanarak matris üzerinden gerçek x,y koordinatlarını (tuple olarak) alıyorum.
            start = tuple(cnt[s][0])
            end = tuple(cnt[e][0])
            far = tuple(cnt[f][0])
            
            # Nesnenin en dış uçlarını yeşil bir çizgi ile birbirine bağlıyorum.
            cv2.line(img, start, end, [0, 255, 0], 2)
            
            # Bulduğum en derin iç noktaya (kusur merkezine) hedefi belli eden yeşil, içi dolu bir daire çizdiriyorum.
            cv2.circle(img, far, 7, [0, 255, 0], -1)

# Oluşturduğum bu sentetik görselleştirmeyi ekranda gösteriyorum.
cv2.imshow("Convexity Defects (Kusur Tespiti)", img)


cv2.waitKey(0)
cv2.destroyAllWindows()
