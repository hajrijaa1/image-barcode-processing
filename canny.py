import cv2

if __name__ == "__main__":
    image = cv2.imread("flowers.PNG")
    cv2.imshow("image window1", image)

    img_edge = cv2.Canny(image, 100, 200)

    cv2.imshow("image window2", img_edge)
    cv2.waitKey(0)
    