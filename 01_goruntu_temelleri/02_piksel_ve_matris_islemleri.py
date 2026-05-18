import cv2
import numpy as np 

# Üzerinde çalışacağımız fotoğrafın dosya yolunu belirliyoruz.
path = "C:\\Users\\muham\\Desktop\\goruntu_isleme\\kodlar\\veri\\istanbul.jpg"

# Görüntümüzü okuyup 'img' değişkenine atıyoruz.
img = cv2.imread(path)

# Görüntünün matris verilerini terminalde görelim.
print("Elimizdeki görüntünün matris değerlerini bastıralım:\n", img)

# Orijinal görüntümüzü ekranda gösteriyoruz.
cv2.imshow("Istanbul - Orijinal Goruntu", img)

# Şimdi elimizdeki görüntünün yüksekliğine, genişliğine ve kaç renk kanalına sahip olduğuna birlikte bakalım.
print("\nElimizdeki görüntünün yükseklik, genişlik ve renk kanalı değerlerine bakalım:", img.shape)

# Bu değerleri daha okunaklı olması için doğru bir sırayla tek tek bastıralım.
print("Görüntümüzün yüksekliğine bakalım =", img.shape[0])
print("Görüntümüzün genişliğine bakalım =", img.shape[1])
print("Görüntümüzün kaç renk kanalına sahip olduğuna bakalım =", img.shape[2])

print("-" * 60)

# Elimizde olan görüntünün 10'a 10 koordinatlarındaki o ufak piksel noktasına odaklanalım.
px = img[10, 10]
print("Görüntümüzün 10'a 10 noktasındaki değeri:", px)

print("-" * 60)

# Fotoğrafın belirli bir kısmını siyaha boyayalım. O alandaki renk değerlerini tamamen 0 yapıp siyah rengine çeviriyoruz.
img[200:300, 200:300] = (0, 0, 0)
cv2.imshow("Belirli Bir Bolgenin Siyah Oldugu Resim", img)

print("-" * 60)

# Orijinal görüntü ile tamamen aynı boyutlarda, içi sıfırlarla (siyahla) dolu yepyeni bir matris oluşturalım.
siyah_tuval = np.zeros(img.shape, dtype="uint8")
cv2.imshow("Siyah Tuval Gorunumu", siyah_tuval)

print("-" * 60)

# Şimdi elimizdeki görüntünün belli bir kesitini alıp, oluşturduğumuz bu siyah tuvalin üzerine yapıştıralım.
kesit = img[250:650, 500:900]
siyah_tuval[250:650, 500:900] = kesit
cv2.imshow("Kesit Eklenmis Olan Siyah Tuval", siyah_tuval)

# Pencerelerin hemen kapanmaması için klavyeden bir tuşa basılmasını bekliyoruz.
cv2.waitKey(0)
cv2.destroyAllWindows()