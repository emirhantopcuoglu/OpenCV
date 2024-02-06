import cv2
import numpy

image = cv2.imread("dog.jpg")

image[50,30] = [255,255,255] # [50,30] noktasinin rgb degeri degistirildi

for i in range(100):
    image[600,i] = [255,255,255]

cv2.imshow("Dog",image)

cv2.waitKey(0)
cv2.destroyAllWindows()