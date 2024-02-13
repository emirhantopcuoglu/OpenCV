import cv2
import numpy

image = numpy.zeros((300,300,3),dtype='uint8') #300x300 boyutlarında siyah (tüm pikselleri sıfır olan) bir görüntü oluşturur.

cv2.line(image,(0,0),(100,100),(20,60,255),3) # çizgi oluşturma

cv2.circle(image,(150,150),25,(0,255,0),2) # daire oluşturma

cv2.putText(image,'PYTHON',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),1)

cv2.imshow('Deneme',image)

cv2.waitKey(0)
cv2.destroyAllWindows()