import cv2
import numpy as np 
from matplotlib import pyplot as plt 

# Üzerinde çalışacağım görüntünün dosya yolunu belirtiyorum.
data_path = "C:\\Users\\muham\\Desktop\\goruntu_isleme\\kodlar\\veri\\istanbul.jpg"

# Görüntüyü okuyup 'img' değişkenine atıyorum.
img = cv2.imread(data_path)

# Orijinal resmi ekranda gösteriyorum.
cv2.imshow("Resmin", img)

# Görüntünün BGR (Blue, Green, Red) renk kanallarını birbirinden ayırıyorum.
b, g, r = cv2.split(img)

# Matplotlib kullanarak her bir renk kanalının piksel yoğunluğunu (histogramını) çizdiriyorum.
# .ravel() ile matrisi tek boyutlu diziye çevirip, 0-256 aralığındaki değerleri hesaplatıyorum.
plt.hist(b.ravel(), 256, [0, 256])
plt.hist(g.ravel(), 256, [0, 256])
plt.hist(r.ravel(), 256, [0, 256])

# Oluşturduğum grafiği ekranda gösteriyorum.
plt.show()

# Pencereleri açık tutmak ve bellekten güvenlice silmek için standart bekleme komutlarım.
cv2.waitKey(0)
cv2.destroyAllWindows()
