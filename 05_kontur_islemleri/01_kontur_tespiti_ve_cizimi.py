import cv2

img = cv2.imread("C:\\Users\\muham\\Desktop\\goruntu_isleme\\kodlar\\veri\\el.jpg")

boyut = cv2.resize(img, (640, 480))

# Kontur tespit algoritmalarının sağlıklı çalışabilmesi için görüntüyü BGR uzayından Gri (Grayscale) tona çeviriyorum.
gray = cv2.cvtColor(boyut, cv2.COLOR_BGR2GRAY)

# Arka plan ile hedef nesneyi (eli) birbirinden tam anlamıyla izole etmek için Threshold (Eşikleme) uyguluyorum.
# 127 eşik değerini kullanarak pikselleri kusursuz bir siyah-beyaz (binary) maskeye dönüştürüyorum.
ret, thresy = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Oluşturduğum bu ikili (binary) matris üzerindeki şekillerin dış sınırlarını (konturlarını) tespit ediyorum.
contours, _ = cv2.findContours(thresy, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Bulduğum bu matematiksel sınırları görselleştirmek adına, orijinal görüntümün üzerine kırmızı renkte (0, 0, 255) çizdiriyorum.
cv2.drawContours(boyut, contours, -1, (0, 0, 255), 3)

# Çıktımı ekranda gösteriyorum.
cv2.imshow("Contour", boyut)

cv2.waitKey(0)
cv2.destroyAllWindows()
