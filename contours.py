import cv2
import numpy as np
  
image = cv2.imread("flowers.PNG")
cv2.waitKey(0)
  
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#primjena canny metode  
edged = cv2.Canny(gray, 30, 200)
cv2.waitKey(0)

#Pronalazak kontura
contours, hierarchy = cv2.findContours(edged, 
    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
  
cv2.imshow('Canny Edges After Contouring', edged)
cv2.waitKey(0)
  
print("Number of Contours found = " + str(len(contours)))

#Crtanje kontura
cv2.drawContours(image, contours, -1, (0, 255, 0), 3)
  
cv2.imshow('Contours', image)
cv2.waitKey(0)
cv2.destroyAllWindows()