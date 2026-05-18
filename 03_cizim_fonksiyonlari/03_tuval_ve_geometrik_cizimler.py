import cv2
import numpy as np

# 512x512 boyutlarında, 3 kanallı (BGR) beyaz bir arka plan (tuval) oluşturuyoruz
canvas = np.zeros((512, 512, 3), dtype=np.uint8) + 255

# Görüntünün sol üst köşesindeki ilk 4 piksel üzerinde renk geçişi (gradyan) denemesi
canvas[0, 0] = (255, 255, 255)  
canvas[0, 1] = (255, 255, 200)  
canvas[0, 2] = (255, 255, 150)  
canvas[0, 3] = (255, 255, 15)   

# Çizgi çizimleri (Parametreler: kaynak matris, start_noktası, end_noktası, renk, kalınlık)
cv2.line(canvas, (50, 50), (512, 512), (255, 0, 0), thickness=5)   
cv2.line(canvas, (100, 50), (200, 255), (0, 0, 255), thickness=7)   

# Dikdörtgen çizimleri (thickness=-1 verilerek şekillerin içi dolduruldu)
cv2.rectangle(canvas, (20, 20), (50, 50), (0, 255, 0), thickness=-1)     
cv2.rectangle(canvas, (50, 50), (150, 150), (0, 255, 0), thickness=-1)   

# Çember çizimi (Merkez: 255,255 - Yarıçap: 100 - Renk: Kırmızı - İçi dolu)
cv2.circle(canvas, (255, 255), 100, (0, 0, 255), thickness=-1)

# Manuel üçgen çizimi için köşe koordinatlarını tanımlıyoruz.
p1 = (100, 200)
p2 = (50, 50)
p3 = (300, 100)

# Tanımladığımız p1, p2 ve p3 noktalarını siyah çizgilerle birleştirerek üçgeni oluşturuyoruz
cv2.line(canvas, p1, p2, (0, 0, 0), 4)
cv2.line(canvas, p2, p3, (0, 0, 0), 4)
cv2.line(canvas, p1, p3, (0, 0, 0), 4)

# Sonucu ekranda gösterip, herhangi bir tuşa basılana kadar pencereyi açık tutuyoruz
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
