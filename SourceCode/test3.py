import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

citra = cv.imread("C:/Users/ACER/Documents/Python/Sample foto/Kucing/kucing.jpg")
color = ('b','g', 'r')
#resize

height = 300
width = 500
dimensi = (width, height)

newCitra = cv.resize(citra, dimensi, interpolation=cv.INTER_LINEAR)
newCitra_gray = cv.cvtColor(newCitra, cv.COLOR_BGR2GRAY)

newCitra_red = newCitra[:,:,2]
newCitra_green = newCitra[:,:,1]
newCitra_blue = newCitra[:,:,0]

print("Resolusi citra lama = ", citra.shape)
print("Resolusi citra baru = ", newCitra.shape)

print("\n\n")
print("matriks citra rgb channel Red")
print(newCitra_red)
print("\n")
print("matriks citra rgb channel Green")
print(newCitra_green)
print("\n")
print("matriks citra rgb channel Blue")
print(newCitra_blue)
print("\n")

print("tinggi yang lama = ", citra.shape[0])
print("lebar yang lama = ", citra.shape[1])

print("tinggi yang baru = ", newCitra.shape[0])
print("lebar yang baru = ", newCitra.shape[1])
print("\n\n")
cv.imshow("citra", citra)
cv.imshow("citra resize", newCitra)
cv.imshow("citra gray", newCitra_gray)
cv.imshow("citra channel Red", newCitra_red)
cv.imshow("citra channel Green", newCitra_green)
cv.imshow("citra channel Blue", newCitra_blue)

#kalkulasi histogram

#menggunakan numpy
histogram_numpy, bins = np.histogram(citra.ravel(), 256, [0,256])
print("perhitungan histogram dengan numpy")
print(histogram_numpy[:])
print("\n")

#menggunakan openCV
histogram_merah = cv.calcHist(citra, [2], None, [256], [0,256]) #[2] untuk mengkalkulasi histogram pada citra rgb pada channel merah saja
histogram_hijau = cv.calcHist(citra, [1], None, [256], [0,256]) #[1] untuk mengkalkulasi histogram pada citra rgb pada channel merah saja
histogram_biru = cv.calcHist(citra, [0], None, [256], [0,256]) #[0] untuk mengkalkulasi histogram pada citra rgb pada channel merah saja

print("hasil kalkulasi histogram citra rgb pada channel merah dengan openCV")
print(histogram_merah[:,0])
print("\n")

print("hasil kalkulasi histogram citra rgb pada channel hijau dengan openCV")
print(histogram_hijau[:,0])
print("\n")

print("hasil kalkulasi histogram citra rgb pada channel biru dengan openCV")
print(histogram_biru[:,0])
print("\n")

#tampil histogram rgb dengan numpy
plt.hist(citra.ravel(), 256, [0,256])
plt.show()

#tampil histogram rgb dengan openCV
for i, col in enumerate(color):
    histogram = cv.calcHist(citra, [i], None, [256], [0,256])
    plt.plot(histogram, color = col)
    plt.xlim([0,256])
plt.show()
    

cv.waitKey()

cv.imwrite("citra resize.jpg", newCitra)