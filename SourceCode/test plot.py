from matplotlib import pyplot as plt #importing pyplot dari library matplotlib dan diganti nama pemanggilan dengan nama "plt"
import cv2 #importing library opencv
import numpy as np #importing library numpy dan diganti nama pemanggilannya dengan nama "np"

color = ('b', 'g', 'r') #membuat variabel yang dapat menyimpan 3 nilai yaitu 'b', 'g', dan 'r'
citra_grayscale = cv2.imread("C:/Users/ACER/Documents/Pemrograman/Python/Sample foto/Kucing/kucing_gray.jpg",0) #membaca file citra rgb dan merubahnya menjadi citra grayscale dengan memasukkan nilai 0 diujungnya
citra_rgb = cv2.imread("C:/Users/ACER/Documents/Pemrograman/Python/Sample foto/Kucing/kucing.jpg") #membaca file citra rgb

histogram = cv2.calcHist(citra_grayscale, [0], None, [256], [0,256]) #Menemukan histogram gambar
print(histogram[:,0])

cv2.imshow("citra_grayscale", citra_grayscale)
cv2.imshow("citra_rgb", citra_rgb)

#mengkalkulasi histogram dengan numpy
histogram, bins = np.histogram(citra_grayscale.ravel(),256,[0,256])

#menampilkan grafik histogram grayscale
plt.hist(citra_grayscale.ravel(),256,[0,256])
plt.show()


#menampilkan grafik histogram 3 channel
print("channel biru")
print(citra_rgb[:,:,0])
print("\n")
print("channel hijau") 
print(citra_rgb[:,:,1])
print("\n")
print("channel merah")
print(citra_rgb[:,:,2])
print("\n")

for i, col in enumerate(color):
    histogram_rgb = cv2.calcHist([citra_rgb], [i], None, [255], [0,255])
    plt.plot(histogram_rgb, color = col)
    plt.xlim([0,256])
plt.show()
    
cv2.waitKey()

