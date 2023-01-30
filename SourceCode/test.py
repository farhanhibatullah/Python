import cv2

gambar_ayang = cv2.imread("D:/Instalasi Software/Python/File/Python/SourceCode/bangun_datar.jpg")
gambar_berdua = cv2.imread("D:/Instalasi Software/Python/File/Python/SourceCode/bangun_datar.jpg")

height = 650
width = 400
dimensi = (width, height)

height2 = 500
width2 = 600
dimensi2 = (width2, height2)

height3 = 400
width3 = 300
dimensi3 = (width3, height3)

newGambar_berdua = cv2.resize(gambar_berdua, dimensi2, interpolation=cv2.INTER_CUBIC)
newGambar_ayang = cv2.resize(gambar_ayang, dimensi, interpolation=cv2.INTER_CUBIC)
ayang_gray = cv2.cvtColor(newGambar_ayang, cv2.COLOR_BGR2GRAY)
ayang_biru = newGambar_ayang[:,:,0]
cropImageAyang = newGambar_ayang[100:650, 0:400]
cropImageBerdua = newGambar_berdua[200:500, 230:400]
res_crop = cv2.resize(cropImageBerdua, dimensi3, interpolation=cv2.INTER_LINEAR)
farhan_blue = res_crop[:,:,0]
farhan_green = res_crop[:,:,1]
farhan_red = res_crop[:,:,2]
farhan_gray = cv2.cvtColor(res_crop, cv2.COLOR_BGR2GRAY)
#cv2.imshow("ayang", newGambar_ayang)
#cv2.imshow("berdua", newGambar_berdua)
cv2.imshow("crop", cropImageBerdua)
cv2.imshow("resize_crop", res_crop)
cv2.imshow("resize_cropBiru", farhan_blue)
cv2.imshow("resize_cropHijau", farhan_green)
cv2.imshow("resize_cropMerah", farhan_red)
cv2.imshow("resize_cropGray", farhan_gray)
#cv2.imshow("ayang_gray", ayang_gray)
#cv2.imshow("ayang_biru", ayang_biru)
#cv2.imshow("ayang_crop", cropImageAyang)

print("pixel asli = ", gambar_ayang.shape)
print("pixel resize = ", newGambar_ayang.shape)
print("height hasil resize = ", newGambar_ayang.shape[0])
print("Hasil konversi = ", farhan_gray.shape)
print("Hasil konversi untuk tinggi = ", farhan_gray.shape[0])
print("Hasil konversi untuk lebar = ", farhan_gray.shape[1])

cv2.waitKey()

cv2.imwrite("ayang biru.jpg", ayang_biru)
cv2.imwrite("farhan_crop.jpg", cropImageBerdua)
cv2.imwrite("farhan_resize.jpg", res_crop)
cv2.imwrite("farhan_red.jpg", farhan_red)
cv2.imwrite("farhan_green.jpg", farhan_green)
cv2.imwrite("farhan_blue.jpg", farhan_blue)
cv2.imwrite("farhan_gray.jpg", farhan_gray)