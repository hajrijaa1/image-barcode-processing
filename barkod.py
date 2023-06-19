import cv2 as cv
from pyzbar import pyzbar

image = cv.imread("barcodee.PNG")

#dekodiramo sliku
barcodes = pyzbar.decode(image)

for barcode in barcodes:
    x,y,w,h = barcode.rect

    #crtamo pravougaonik okolo koda - (255,0,0) za plavu boju okolo
    cv.rectangle(image, (x,y), (x+w, y+h), (255,0,0), 4)

    #pretvaranje u string
    bdata = barcode.data.decode("utf-8")
    btype = barcode.type
    text = f"{bdata}, {btype}"
    print("----")
    print(text)
    print("----")
    
    cv.putText(image, text,(x,y-10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),0)

cv.imshow("image", image)
cv.waitKey(0)
