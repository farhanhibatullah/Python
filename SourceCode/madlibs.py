import cv2
import numpy as np
from matplotlib import pyplot as plt

color = ('b', 'g', 'r')
citra = cv2.imread("D:/Instalasi Software/Python/File/Python/Sample foto/Farhan/farhan_resize.jpg")
citra2 = cv2.imread("D:/Instalasi Software/Python/File/Python/Sample foto/Berdua/berdua.jpg")

height = 500
width = 800
dimensi = (width, height)

new_citra2 = cv2.resize(citra2, dimensi, interpolation=cv2.INTER_LINEAR)

hist_num, bins = np.histogram(new_citra2.ravel(), 256, [0,256])
print(hist_num[:])

#citra 1

cv2.imshow("citra", citra)
plt.hist(citra.ravel(), 256, [0,256])
plt.show()

for i, col in enumerate(color):
    histogram = cv2.calcHist(citra, [i], None, [256], [0,256])
    plt.plot(histogram, color = col)
    plt.xlim([0,256])
plt.show()

#citra 2

cv2.imshow("citra2", new_citra2)

plt.hist(new_citra2.ravel(),256,[0,256])
plt.show()


for i, col in enumerate(color):
    hist_citra2 = cv2.calcHist(new_citra2, [i], None, [256], [0,256])
    plt.plot(hist_citra2, color = col)
    plt.xlim([0,256])
plt.show()


cv2.waitKey()

#menyimpan gambar pada specified path untuk cv2.imwrite
path = "C:/Users/ACER/Documents/Python/Sample foto/Hania"
#cv2.imwrite(os.path.join(path,"berdua resize.jpg"), new_citra2)