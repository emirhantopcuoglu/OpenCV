import cv2

image = cv2.imread("photo.jpg")

meanFilter = cv2.blur(image, (10,10))  # Mean filter işlemi
medianFilter = cv2.medianBlur(image,3) # Median filter işlemi
gauss = cv2.GaussianBlur(image,(3,3),0) # Gauss filter işlemi

cv2.imshow("Original Photo", image)
cv2.imshow("Mean Filtered Photo", meanFilter)
cv2.imshow("Median Filtered Photo", medianFilter)
cv2.imshow("Gauss Filtered Photo", gauss)

cv2.waitKey(0)
cv2.destroyAllWindows()
