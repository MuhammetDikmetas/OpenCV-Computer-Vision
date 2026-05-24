import cv2


data_path = "C:\\Users\\muham\\Desktop\\goruntu_isleme\\kodlar\\veri\\trafik.mp4"
video = cv2.VideoCapture(data_path)

while True:
    
    ret, frame = video.read()
    
    # Video bittiğinde OpenCV'nin hata verip programı çökertmemesi için döngüyü kırıyorum.
    if not ret:
        break
    
    
    frame = cv2.flip(frame, 1)
    
    # Ekrana sığdırmak için matris boyutunu küçültüyorum.
    frame = cv2.resize(frame, (640, 480))
    
    # Görüntüdeki nesnelerin sınırlarını (kenarlarını) tespit etmek için Canny algoritmasını uyguluyorum.
    # Alt eşik değerini 100, üst eşik değerini 200 olarak belirliyorum.
    kenarlar = cv2.Canny(frame, 100, 200)
    
    
    cv2.imshow("Orijinal Trafik Goruntusu", frame)
    cv2.imshow("Canny Kenar Tespiti", kenarlar)
    
   
    if cv2.waitKey(5) & 0xFF == ord("q"):
        break
    

video.release()
cv2.destroyAllWindows()
