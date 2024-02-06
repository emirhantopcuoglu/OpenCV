import cv2
import numpy

image = cv2.imread("BrooklynBridge.jpg")

section = image[50:550,300:700] # gorselin bir kismini section degiskenine atar

cv2.imshow("Section",section)
cv2.imshow("Brooklyn Bridge",image)

cv2.waitKey(0)
cv2.destroyAllWindows()