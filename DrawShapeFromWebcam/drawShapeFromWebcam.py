import cv2
import numpy

camera = cv2.VideoCapture(0)

while True:
    ret,frame = camera.read()

    cv2.rectangle(frame,(100,100),(200,200),(0,0,255),2) # dortgen oluşturma
    cv2.line(frame,(0,0),(100,100),(20,60,255),3) # çizgi oluşturma
    cv2.circle(frame,(150,150),25,(0,255,0),2) # daire oluşturma
    cv2.putText(frame,'PYTHON',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),1) # text oluşturma

    cv2.imshow('Video',frame)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
camera.release()

cv2.destroyAllWindows()