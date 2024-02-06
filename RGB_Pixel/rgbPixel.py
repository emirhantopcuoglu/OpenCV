import cv2
import numpy

image = cv2.imread("cat.jpg")

cv2.imshow("Cat", image)
print(image[(230,80)]) # Gorselin sol kosesi referans alinarak 230 piksel asagida, 80 piksel sagda kalan noktanın rgb degerini verir

cv2.waitKey(0)
cv2.destroyAllWindows()