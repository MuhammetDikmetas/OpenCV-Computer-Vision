import cv2
import numpy as np 


data_path = "C:\\Users\\muham\\Desktop\\goruntu_isleme\\kodlar\\veri\\afrika.jpg"
img = cv2.imread(data_path)


img = cv2.resize(img, (640, 480))

# Kontur ve Hull işlemlerinin sağlıklı çalışması için görüntümü BGR uzayından Gri (Grayscale) tona çeviriyorum.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Görüntüdeki parazitleri (noise) azaltmak ve daha pürüzsüz konturlar elde etmek için hafif bir yumuşatma (blur) uyguluyorum.
blur = cv2.blur(gray, (3, 3))

# Arka planı izole edip nesne sınırlarını netleştirmek için Binary Threshold (Eşikleme) işlemi gerçekleştiriyorum.
ret, thresh = cv2.threshold(blur, 40, 255, cv2.THRESH_BINARY)

# Eşiklenmiş siyah-beyaz matris üzerindeki tüm nesne sınırlarını (konturları) tespit ediyorum.
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Her bir kontur için hesaplayacağım dışbükey örtü (Convex Hull) noktalarını tutmak üzere boş bir liste oluşturuyorum.
hull = []

# Tespit ettiğim tüm konturları bir döngüye sokup, her biri için en dar dışbükey poligonu hesaplayarak listeme ekliyorum.
for i in range(len(contours)):
    hull.append(cv2.convexHull(contours[i], False))

# Orijinal resim yerine sonuçları çok daha net görebilmek için, matrisimle aynı boyutlarda tamamen siyah, boş bir tuval (arka plan) oluşturuyorum.
bg = np.zeros((thresh.shape[0], thresh.shape[1], 3), np.uint8)

for i in range(len(contours)):
    # Tespit ettiğim orijinal nesne sınırlarını (konturları) tuvalime mavi renkte çizdiriyorum.
    cv2.drawContours(bg, contours, i, (255, 0, 0), 3, 8, hierarchy)
    
    # Hesapladığım Convex Hull (Dışbükey Örtü) poligonlarını ise aynı tuvale yeşil renkte çizdiriyorum.
    cv2.drawContours(bg, hull, i, (0, 255, 0), 1, 8)
    
# Oluşturduğum bu sentetik tuvali ekranda gösteriyorum.
cv2.imshow("Convex Hull (Disbukey Ortu)", bg)


cv2.waitKey(0)
cv2.destroyAllWindows()
