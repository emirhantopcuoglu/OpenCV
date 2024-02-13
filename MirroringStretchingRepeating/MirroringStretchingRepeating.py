import cv2
import numpy

image = cv2.imread("Brandenburg.jpg")

mirroringImage = cv2.copyMakeBorder(image,1000,1000,1000,1000,cv2.BORDER_REFLECT)
stretchingImage = cv2.copyMakeBorder(image,500,500,500,500,cv2.BORDER_REPLICATE)
repeatingImage = cv2.copyMakeBorder(image,1000,1000,1000,1000,cv2.BORDER_WRAP)
framingImage = cv2.copyMakeBorder(image,50,50,50,50,cv2.BORDER_CONSTANT)

cv2.imshow("Brandenburg Gate",mirroringImage)
cv2.imshow("Brandenburg Gate",stretchingImage)
cv2.imshow("Brandenburg Gate",repeatingImage)
cv2.imshow("Brandenburg Gate",framingImage)

cv2.waitKey(0)
cv2.destroyAllWindows()