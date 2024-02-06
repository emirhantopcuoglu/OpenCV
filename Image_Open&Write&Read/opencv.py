import cv2
import numpy

image = cv2.imread("landscape.jpg",0) # imread fonksiyonu ile bir dosyadan goruntu okunur, 0 paramatresi eklenirs renkler kullanilmaz

cv2.imshow("Landscape",image) # imshow fonksiyonu ile goruntu gosterilir

cv2.imwrite("new_landscape.png",image) # Goruntuyu kaydetmek icin kullanilir

print(image) # Gorunutunun piksel degerlerini (matrisleri) yazdirir

print(image.size) # Goruntunun piksel sayisini yazdirir

print(image.dtype) # Bir NumPy dizisinin veri tipini dondurur

print(image.shape) # Goruntunun genislik, yukseklik ve renk kanal sayisini dondurur

cv2.waitKey(0) # Kullanici bir tusa basana kadar bekleyerek pencereyi acik tutar

cv2.destroyAllWindows() # Pencereyi kapatir
