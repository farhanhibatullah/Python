import cv2
"""

print("Default path = D:\Instalasi Software\Python\File\Python\SourceCode\bangun_datar.jpg")
print("Ubah menjadi = D:/Instalasi Software/Python/File/Python/SourceCode/bangun_datar.jpg")
path = input("Masukkan path anda = ")

"""

image = cv2.imread("D:/Instalasi Software/Python/File/Python/SourceCode/bangun_datar.jpg")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, image_thresh = cv2.threshold(gray_image, 220, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(image_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
approx1 = cv2.approxPolyDP(cnt1, 0.02*cv2.arcLength(cnt1,True), True)
for i, contour in enumerate(contours):
    if i == 0:
        continue
    epsilon = 0.01*cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)
    
    cv2.drawContours(image, [approx1], -1, (0,0,0), 4)
    
    x, y, w, h = cv2.boundingRect(approx)
    x_mid = int(x + w/3)
    y_mid = int(y + h/1.5)
    
    coords = (x_mid, y_mid)
    colour = 1
    font = cv2.FONT_HERSHEY_DUPLEX
    
if len(approx) == 3:
    cv2.putText(image, "Segitiga", coords, font,1, colour, 1)
    
elif len(approx) == 4:
    cv2.putText(image, "Segi Empat", coords, font, 1, colour, 1)
    
elif len(approx) == 5:
    cv2.putText(image, "Pentagon", coords, font, 1, colour, 1)
    
elif len(approx) == 6:
    cv2.putText(image, "Hexagon", coords, font, 1, colour, 1)
    
elif len(approx) == 7:
    cv2.putText(image, "Segi Tujuh", coords, font,1, colour, 1)
    
elif len(approx) == 8:
    cv2.putText(image, "Segi Delapan", coords, font,1, colour, 1)
    
else:
    cv2.putText(image, "Lingkaran", coords,font, 1, colour, 1)
    
cv2.imshow("Gambar", image)

cv2.waitKey(0)