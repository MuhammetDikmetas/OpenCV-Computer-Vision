import cv2
import numpy as np 

# Üzerinde çalışacağım trafik videosunu projeye dahil ediyorum.
data_path = "C:\\Users\\muham\\Desktop\\goruntu_isleme\\kodlar\\veri\\trafik.mp4"
goruntu = cv2.VideoCapture(data_path)

# Trackbar'ların çalışabilmesi için zorunlu olan boş fonksiyonumu tanımlıyorum.
def nothing(x):
    pass

# HSV eşik değerlerini dinamik olarak ayarlayacağım kontrol panelini oluşturuyorum.
cv2.namedWindow("Trackbar")
cv2.resizeWindow("Trackbar", 600, 600)

# Renk, doygunluk ve parlaklık (HSV) için alt limit (Lower) kızaklarını ekliyorum.
cv2.createTrackbar("Lower-H", "Trackbar", 0, 180, nothing)
cv2.createTrackbar("Lower-S", "Trackbar", 0, 255, nothing)
cv2.createTrackbar("Lower-V", "Trackbar", 0, 255, nothing)

# Aynı şekilde üst limit (Upper) kızaklarını oluşturuyorum.
cv2.createTrackbar("Upper-H", "Trackbar", 0, 180, nothing)
cv2.createTrackbar("Upper-S", "Trackbar", 0, 255, nothing)
cv2.createTrackbar("Upper-V", "Trackbar", 0, 255, nothing)

# Üst limit kızaklarının varsayılan değerlerini en tepeye çekiyorum.
cv2.setTrackbarPos("Upper-H", "Trackbar", 180)
cv2.setTrackbarPos("Upper-S", "Trackbar", 255)
cv2.setTrackbarPos("Upper-V", "Trackbar", 255)

while True:
    ret, frame = goruntu.read()
    
    # Video bittiğinde döngünün programı çökertmemesi için kontrol ekliyorum.
    if not ret:
        break
    
    # Görüntüyü aynalayıp, işlem maliyetini düşürmek için matris boyutunu ufaltıyorum.
    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (640, 480))
    
    # Işıktan bağımsız sırf renge odaklanmak için BGR uzayından HSV uzayına geçiyorum.
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Trackbar'dan anlık eşik değerlerini (kullanıcı seçimlerini) okuyorum.
    lower_h = cv2.getTrackbarPos("Lower-H", "Trackbar")
    lower_s = cv2.getTrackbarPos("Lower-S", "Trackbar")
    lower_v = cv2.getTrackbarPos("Lower-V", "Trackbar")
    
    upper_h = cv2.getTrackbarPos("Upper-H", "Trackbar")
    upper_s = cv2.getTrackbarPos("Upper-S", "Trackbar")
    upper_v = cv2.getTrackbarPos("Upper-V", "Trackbar")
    
    # Okunan bu değerleri OpenCV'nin işleyebileceği NumPy dizilerine çeviriyorum.
    lower_color = np.array([lower_h, lower_s, lower_v])
    upper_color = np.array([upper_h, upper_s, upper_v])
    
    # Belirlediğim HSV aralığındaki pikselleri beyaz (255), dışında kalanları siyah (0) yapıyorum.
    mask = cv2.inRange(frame_hsv, lower_color, upper_color)
    
    # Orijinal görüntüyü ve oluşturduğum filtre maskesini ekranda gösteriyorum.
    cv2.imshow("Original", frame)
    cv2.imshow("Mask", mask)

    # Saniyede yaklaşık 50 kez klavyeyi dinleyip, 'q' tuşuna basıldığında döngüyü kırıyorum.
    if cv2.waitKey(20) & 0xFF == ord("q"):
        break
        
# Videoyu serbest bırakıp bellekten pencereleri temizliyorum.
goruntu.release()
cv2.destroyAllWindows()
