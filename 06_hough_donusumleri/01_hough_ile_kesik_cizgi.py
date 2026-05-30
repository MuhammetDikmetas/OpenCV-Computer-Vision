import cv2
import numpy as np 


data_path = "C:\\Users\\muham\\Desktop\\goruntu_isleme\\kodlar\\veri\\kesik_cizgiler.jpg"

img = cv2.imread(data_path)


img = cv2.resize(img, (640, 480))

# Hough dönüşümü öncesinde algoritmaların doğru çalışabilmesi için görüntümü Gri (Grayscale) tona çeviriyorum.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Çizgileri tespit etmeden önce resimdeki nesnelerin ana kenarlarını (hatlarını) Canny algoritmasıyla buluyorum.
# 75 alt eşik (silinenler), 150 üst eşik (kesin kenarlar) olarak ayarlıyorum.
edges = cv2.Canny(gray, 75, 150)

# Olasılıksal Hough Dönüşümü (HoughLinesP) kullanarak kesik çizgileri tespit edip birleştiriyorum.
# maxLineGap=200 parametresi ile çizgiler arasındaki kopuklukları/boşlukları tolere edip tek bir çizgi gibi algılanmasını sağlıyorum.
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, maxLineGap=200)

# Algoritmanın bulduğu tüm çizgiler üzerinde bir döngü başlatıyorum.
for line in lines:
    # Tespit edilen her bir çizginin başlangıç (x1, y1) ve bitiş (x2, y2) koordinatlarını alıyorum.
    x1, y1, x2, y2 = line[0]
    
    # Bu koordinatları kullanarak orijinal matrisim üzerine kalınlığı 2 olan yeşil çizgiler çizdiriyorum.
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
    
# Orijinal görüntüyü, gri tonlu halini ve Canny ile çıkarılmış kenar maskesini pencerelerde gösteriyorum.
cv2.imshow("HoughLinesP (Orijinal Uzerine Cizim)", img)
cv2.imshow("Grayscale", gray) 
cv2.imshow("Canny Edges", edges)


cv2.waitKey(0)
cv2.destroyAllWindows()
