import cv2
import numpy as np


data_path = "C:\\Users\\muham\\Desktop\\goruntu_isleme\\kodlar\\veri\\sari_cizgili_yol.mp4"
videom = cv2.VideoCapture(data_path)

while True:
    ret, frame = videom.read()
    
    if not ret:
        break
    
    frame = cv2.resize(frame, (640, 480))
    
    # Işık ve gölge değişimlerinden etkilenmeden renk tespiti yapabilmek için BGR'dan HSV renk uzayına geçiyorum.
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Şeritlerin (sarı renk) matris üzerindeki HSV alt ve üst limitlerini belirliyorum.
    lower_yellow = np.array([15, 100, 100], np.uint8)
    upper_yellow = np.array([32, 255, 255], np.uint8)
    
    # Bu sınırları kullanarak sadece sarı şeritlerin beyaz, geri kalanın siyah olduğu bir maske oluşturuyorum.
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    
    # Hough dönüşümünün düzgün çalışabilmesi için öncelikle maskelenmiş görüntünün ana kenarlarını Canny algoritmasıyla buluyorum.
    edges = cv2.Canny(mask, 75, 250)
    
    # Olasılıksal Hough Dönüşümü (HoughLinesP) ile tespit edilen kenarlar üzerindeki düz çizgileri (şeritleri) matematiksel olarak hesaplıyorum.
    # maxLineGap=50 ile kesik şeritler arasındaki küçük kopuklukları tolere ediyorum.
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, maxLineGap=50)
    
    # Eğer matris üzerinde çizgi (şerit) bulunmuşsa, bunları orijinal görüntümün üzerine çizdiriyorum.
    if lines is not None:
        for line in lines:
            (x1, y1, x2, y2) = line[0]
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
    
    
    cv2.imshow("Canny Edges", edges)
    cv2.imshow("Sari Maske", mask)
    cv2.imshow("Serit Takibi (Sonuc)", frame) 

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Kullanıcı çıkış yaptı.")
        break

videom.release()
cv2.destroyAllWindows()
