import cv2

gambar = cv2.imread("C:/Users/ACER/Documents/Python/kucing.jpg")

gambar_gray = cv2.cvtColor(gambar, cv2.COLOR_BGR2GRAY)

cv2.imshow("kucing gray", gambar_gray)

cv2.waitKey()