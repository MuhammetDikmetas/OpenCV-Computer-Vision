import cv2
import numpy as np 


data_path = "C:\\Users\\muham\\Desktop\\goruntu_isleme\\kodlar\\veri\\yuvarlak_cisim1.jpg"
img = cv2.imread(data_path)


img = cv2.resize(img, (640, 480))

# Hough algoritmalarının matematiksel altyapısı renklerle değil yoğunluklarla çalıştığı için görüntümü BGR uzayından Grayscale (Gri) tona indirgiyorum.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# HoughCircles algoritması piksel gürültülerine (noise) karşı çok hassas olduğu için medyan bulanıklaştırma (medianBlur) filtresinden geçiriyorum.
blurlama = cv2.medianBlur(gray, 5)

# Görseldeki iç içe geçmiş topları doğru tespit edebilmek için algoritma parametrelerine mühendislik dokunuşu yapıyorum.
# Merkezler arası mesafeyi 20'ye, kusursuzluk beklentimi (param2) 25'e indirip yarıçap toleransını (5-40) görselime özel optimize ediyorum.
circles = cv2.HoughCircles(blurlama, cv2.HOUGH_GRADIENT, 1, 20, param1=100, param2=25, minRadius=5, maxRadius=40)


if circles is not None:
    # Algoritmanın bulduğu ondalıklı koordinat değerlerini çizim yapabilmek için 16-bit tam sayılara (uint16) yuvarlıyorum.
    circles = np.uint16(np.around(circles))
    
    # Tespit ettiğim tüm çemberlerin üzerinde dönüyorum.
    for i in circles[0, :]:
        # Nesnenin dış sınırlarını jilet gibi yeşil (0, 255, 0) renkte çizdiriyorum.
        cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
        
        # Nesnenin tam ağırlık merkezine kırmızı (0, 0, 255) renkli hedef noktamı koyuyorum.
        cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)


cv2.imshow("Hough Circles (Optimize Edilmis)", img)


cv2.waitKey(0)
cv2.destroyAllWindows()
