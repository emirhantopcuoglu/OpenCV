import cv2
import numpy

# Eğer video dosyasını kullanmak istiyorsanız, dosya adını belirtin (örneğin: "video.mp4")
# Eğer kamera kullanmak istiyorsanız, kamera indeksini belirtin (örneğin: 0)
camera = cv2.VideoCapture(0)

while(True):
    # Her bir kareyi okuyun
    ret,frame=camera.read()
    # kareyi ekrana gösterin
    cv2.imshow('Video',frame)

    # 'q' tuşuna basıldığında döngüyü sonlandırın
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Video yakalama nesnesini serbest bırakın ve pencereyi kapatın
camera.release()
cv2.destroyAllWindows()