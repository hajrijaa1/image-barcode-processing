import cv2

image = cv2.imread("flowers.PNG")
window_name = "Image"
ksize = (10, 10)
cv2.imshow("image window1", image)
#Primjena blur metode
img = cv2.blur(image, ksize, cv2.BORDER_DEFAULT)


cv2.imshow("image window2", img)
cv2.waitKey(0)
