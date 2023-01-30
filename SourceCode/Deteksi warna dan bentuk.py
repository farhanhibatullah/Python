import cv2
import numpy as np
def empty(img):
    pass

video = cv2.VideoCapture(0)
cv2.namedWindow("Detection")
cv2.resizeWindow("Detection", 600, 300)
cv2.createTrackbar("hue_min", "Detection", 0,179, empty)
cv2.createTrackbar("hue_max", "Detection", 179,179, empty)
cv2.createTrackbar("sat_min", "Detection", 0,255, empty)
cv2.createTrackbar("sat_max", "Detection", 255,255, empty)
cv2.createTrackbar("val_min", "Detection", 0,255, empty)
cv2.createTrackbar("val_max", "Detection", 255,255, empty)

while True:
    ret,img = video.read()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hue_min = cv2.getTrackbarPos("hue_min","Detection")
    hue_max = cv2.getTrackbarPos("hue_max","Detection")
    sat_min = cv2.getTrackbarPos("sat_min","Detection")
    sat_max = cv2.getTrackbarPos("sat_max","Detection")
    val_min = cv2.getTrackbarPos("val_min","Detection")
    val_max = cv2.getTrackbarPos("val_max","Detection")
    lower = np.array([hue_min, sat_min, val_min])
    upper = np.array([hue_max, sat_max, val_max])
    mask = cv2.inRange(hsv, lower, upper)
    contours, hei = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for c in contours:
        area = cv2.contourArea(c)
        if area>300:
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.02*peri, True)
            x,y,w,h = cv2.boundingRect(c)
            cv2.rectangle = (img, (x,y), (x+w, y+h), (0,255,0), 2)
            cv2.putText(img, "Point: " + str(len(approx)), (x+w-20, y+h-45), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,255,0), 2)
            print(" ")
        if len(approx)==4:
            cv2.putText(img, "Rectangle", (x+w+20, y+h+45), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,255,0), 2)
        elif len(approx)==3:
            cv2.putText(img, "Triangle", (x+w+20, y+h+45), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,255,0), 2) 
        else:
            cv2.putText(img, "Circle", (x+w+20, y+h+45), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,255,0), 2)
    cv2.imshow("Frame", img)
    cv2.imshow("Mask", mask)
    k=cv2.waitKey(1)
    if k==ord('q'):
        break

video.release()
cv2.destroyAllWindows()