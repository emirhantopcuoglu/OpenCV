import cv2
import numpy

image = cv2.imread("Istanbul.jpg")
"""
image[:,:,0] = 255 # mavi efekt
image[:,:,1] = 255 # yesil efekt
image[:,:,2] = 255 # kirmizi efekt 
"""

image[300:500,600:900,0] = 255 # belli bir kisma efekt uygulama

cv2.imshow("Istanbul",image)

cv2.waitKey(0)
cv2.destroyAllWindows()