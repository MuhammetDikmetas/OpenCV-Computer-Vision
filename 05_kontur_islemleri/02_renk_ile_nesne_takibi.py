import cv2
import numpy as np


cap = cv2.VideoCapture("C:\\Users\\muham\\Desktop\\goruntu_isleme\\kodlar\\veri\\dog.mp4")


while True:
    
    ret, frame = cap.read()
    
    
    if not ret:
        break
        
    
    frame = cv2.resize(frame, (640, 480))
        
    # Renkleri ışık değişimlerinden bağımsız olarak izole edebilmek için BGR uzayından HSV uzayına geçiyorum.
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Videodaki beyaz nesneyi (köpeği) tespit edebilmek için beyaz rengin HSV alt ve üst limitlerini belirliyorum.
    lower_white = np.array([0, 0, 150])
    upper_white = np.array([179, 60, 255])
    
    # Belirlediğim bu HSV sınırlarını kullanarak arka planı siyah, hedef nesneyi beyaz yapan bir maske (filtre) oluşturuyorum.
    mask = cv2.inRange(hsv, lower_white, upper_white)
    
    # Orijinal matrisim ile maskemi 'Bitsel VE' (Bitwise AND) işlemine sokarak, görüntünün sadece maskelenen kısımlarını renkli olarak çekip alıyorum.
    res = cv2.bitwise_and(frame, frame, mask=mask)
    
    # Orijinal görüntüyü, oluşturduğum maskeyi ve bitwise işlemi sonrası ortaya çıkan sonucu pencerelerde gösteriyorum.
    cv2.imshow("Orijinal Video", frame)
    cv2.imshow("Siyah Beyaz Maske", mask)
    cv2.imshow("Renk Odakli Takip (Result)", res)
    
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27 or k == ord('q'): 
        break

cap.release()
cv2.destroyAllWindows()
