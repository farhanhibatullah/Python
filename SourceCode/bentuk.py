import cv2
import numpy as np

cap = cv2.VideoCapture(0)
"""
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
"""
while True:
    ret, frame = cap.read(0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([90,165,131])
    upper_blue = np.array([121, 255, 255])
    lower_red = np.array([170,71,170])
    upper_red = np.array([180,180,255])
    lower_green = np.array([38,55,111])
    upper_green = np.array([75,255,255])
    lower_yellow = np.array([22,130,85])
    upper_yellow = np.array([33,255,255])
    lower_pink = np.array([150,75,195])
    upper_pink = np.array([170,255,255])
    lower_brown = np.array([0,93,94])
    upper_brown = np.array([24,254,255])
    lower_orange = np.array([8,149,147])
    upper_orange = np.array([27,255,255])
    lower_white = np.array([0,0,189])
    upper_white = np.array([200,22,255])
    lower_purple = np.array([142,0,156])
    upper_purple = np.array([148,255,255])
    lower_gray = np.array([83,34,113])
    upper_gray = np.array([113,111,255])
    lower_black = np.array([54,9,67])
    upper_black = np.array([127,89,133])
    
    mask1 = cv2.inRange(hsv, lower_blue, upper_blue)
    mask2 = cv2.inRange(hsv, lower_red, upper_red)
    mask3 = cv2.inRange(hsv, lower_green, upper_green)
    mask4 = cv2.inRange(hsv, lower_yellow, upper_yellow)
    mask5 = cv2.inRange(hsv, lower_pink, upper_pink)
    mask6 = cv2.inRange(hsv, lower_brown, upper_brown)
    mask7 = cv2.inRange(hsv, lower_orange, upper_orange)
    mask8 = cv2.inRange(hsv, lower_white, upper_white)
    mask9 = cv2.inRange(hsv, lower_purple, upper_purple)
    mask10 = cv2.inRange(hsv, lower_gray, upper_gray)
    mask11 = cv2.inRange(hsv, lower_black, upper_black)
    kernel1 = np.ones((10,10), np.uint8)
    kernel2 = np.ones((6,6), np.uint8)
    
    mask1 = cv2.erode(mask1, kernel1)
    mask1 = cv2.dilate(mask1, kernel2)
    mask2 = cv2.erode(mask2, kernel1)
    mask2 = cv2.dilate(mask2, kernel2)
    mask3 = cv2.erode(mask3, kernel1)
    mask3 = cv2.dilate(mask3, kernel2)
    mask4 = cv2.erode(mask4, kernel1)
    mask4 = cv2.dilate(mask4, kernel2)
    mask5 = cv2.erode(mask5, kernel1)
    mask5 = cv2.dilate(mask5, kernel2)
    mask6 = cv2.erode(mask6, kernel1)
    mask6 = cv2.dilate(mask6, kernel2)
    mask7 = cv2.erode(mask7, kernel1)
    mask7 = cv2.dilate(mask7, kernel2)
    mask8 = cv2.erode(mask8, kernel1)
    mask8 = cv2.dilate(mask8, kernel2)
    mask9 = cv2.erode(mask9, kernel1)
    mask9 = cv2.dilate(mask9, kernel2)
    mask10 = cv2.erode(mask10, kernel1)
    mask10 = cv2.dilate(mask10, kernel2)
    mask11 = cv2.erode(mask11, kernel1)
    mask11 = cv2.dilate(mask1, kernel2)
    
    cont1, hier = cv2.findContours(mask1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cont2, hier = cv2.findContours(mask2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cont3, hier = cv2.findContours(mask3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cont4, hier = cv2.findContours(mask4, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cont5, hier = cv2.findContours(mask5, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cont6, hier = cv2.findContours(mask6, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cont7, hier = cv2.findContours(mask7, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cont8, hier = cv2.findContours(mask8, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cont9, hier = cv2.findContours(mask9, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cont10, hier = cv2.findContours(mask10, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cont11, hier = cv2.findContours(mask11, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt1 in cont1:
        
        area1 = cv2.contourArea(cnt1)
        approx1 = cv2.approxPolyDP(cnt1, 0.02*cv2.arcLength(cnt1,True), True)
        M1 = cv2.moments(cnt1)
        cX1 = int(M1["m10"]/M1["m00"])
        cY1 = int (M1["m01"]/M1["m00"])
        #cv2.putText(frame, "Blue", (cX1-20,cY1-20),cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0), 2)
        #cv2.circle(frame, (cX1, cY1), 7, (255,0,0), -1)
        cv2.drawContours(frame, [approx1], -1, (255,0,0), 3)
        
        """
        if area1> 400:
            
            if len(approx1) == 3:
                cv2.putText(frame, "Triangle", (cX1+20, cY1+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
            elif len(approx1) == 4:
                cv2.putText(frame, "Rectangle", (cX1+20, cY1+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)    
            elif len(approx1) == 5:
                cv2.putText(frame, "Pentagon", (cX1+20, cY1+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
            elif len(approx1) == 6:
                cv2.putText(frame, "Hexagon", (cX1+20, cY1+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
            elif len(approx1) == 10:
                cv2.putText(frame, "Star", (cX1+20, cY1+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)                    
            else:
                cv2.putText(frame, "Circle", (cX1+20, cY1+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)  
        """
    for cnt2 in cont2:
        
        area2 = cv2.contourArea(cnt2)
        approx2 = cv2.approxPolyDP(cnt2, 0.02*cv2.arcLength(cnt2,True), True)
        M2 = cv2.moments(cnt2)
        cX2 = int(M2["m10"]/M2["m00"])
        cY2 = int (M2["m01"]/M2["m00"])
        #cv2.putText(frame, "Red", (cX2-20,cY2-20),cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
        #cv2.circle(frame, (cX2, cY2), 7, (0,0,255), -1)
        cv2.drawContours(frame, [approx2], -1, (0,0,255), 3)
        
        """
        if area2> 400:
            
            if len(approx2) == 3:
                cv2.putText(frame, "Triangle", (cX2+20, cY2+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
            elif len(approx2) == 4:
                cv2.putText(frame, "Rectangle", (cX2+20, cY2+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)    
            elif len(approx2) == 5:
                cv2.putText(frame, "Pentagon", (cX2+20, cY2+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
            elif len(approx2) == 6:
                cv2.putText(frame, "Hexagon", (cX2+20, cY2+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
            elif len(approx2) == 10:
                cv2.putText(frame, "Star", (cX2+20, cY2+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)                    
            else:
                cv2.putText(frame, "Circle", (cX2+20, cY2+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)               
        """
             
    for cnt3 in cont3:
        
        area3 = cv2.contourArea(cnt3)
        approx3 = cv2.approxPolyDP(cnt3, 0.02*cv2.arcLength(cnt3,True), True)
        M3 = cv2.moments(cnt3)
        cX3 = int(M3["m10"]/M3["m00"])
        cY3 = int (M3["m01"]/M3["m00"])
        #cv2.putText(frame, "Green", (cX3-20,cY3-20),cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
        #cv2.circle(frame, (cX3, cY3), 7, (0,255,0), -1)
        cv2.drawContours(frame, [approx3], -1, (0,255,0), 3)
        
        """
        if area3> 400:
            
            if len(approx3) == 3:
                cv2.putText(frame, "Triangle", (cX3+20, cY3+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
            elif len(approx3) == 4:
                cv2.putText(frame, "Rectangle", (cX3+20, cY3+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)    
            elif len(approx3) == 5:
                cv2.putText(frame, "Pentagon", (cX3+20, cY3+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
            elif len(approx3) == 6:
                cv2.putText(frame, "Hexagon", (cX3+20, cY3+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
            elif len(approx3) == 10:
                cv2.putText(frame, "Star", (cX3+20, cY3+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)                    
            else:
                cv2.putText(frame, "Circle", (cX3+20, cY3+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)            
        """     
                
    for cnt4 in cont4:
        
        area4 = cv2.contourArea(cnt4)
        approx4 = cv2.approxPolyDP(cnt4, 0.02*cv2.arcLength(cnt4,True), True)
        M4 = cv2.moments(cnt4)
        cX4 = int(M4["m10"]/M4["m00"])
        cY4 = int (M4["m01"]/M4["m00"])
        #cv2.putText(frame, "Yellow", (cX4-20,cY4-20),cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,255), 2)
        #cv2.circle(frame, (cX4, cY4), 7, (0,255,255), -1)
        cv2.drawContours(frame, [approx4], -1, (0,255,255), 3)
        
        """
        if area4> 400:
            
            if len(approx4) == 3:
                cv2.putText(frame, "Triangle", (cX4+20, cY4+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
            elif len(approx4) == 4:
                cv2.putText(frame, "Rectangle", (cX4+20, cY4+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)    
            elif len(approx4) == 5:
                cv2.putText(frame, "Pentagon", (cX4+20, cY4+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
            elif len(approx4) == 6:
                cv2.putText(frame, "Hexagon", (cX4+20, cY4+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
            elif len(approx4) == 10:
                cv2.putText(frame, "Star", (cX4+20, cY4+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)                    
            else:
                cv2.putText(frame, "Circle", (cX4+20, cY4+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)                           
        """
             
    for cnt5 in cont5:
        
        area5 = cv2.contourArea(cnt5)
        approx5 = cv2.approxPolyDP(cnt5, 0.02*cv2.arcLength(cnt5,True), True)
        M5 = cv2.moments(cnt5)
        cX5 = int(M5["m10"]/M5["m00"])
        cY5 = int (M5["m01"]/M5["m00"])
        #cv2.putText(frame, "Pink", (cX5-20,cY5-20),cv2.FONT_HERSHEY_COMPLEX, 1, (203,192,255), 2)
        #cv2.circle(frame, (cX5, cY5), 7, (203,192,255), -1)
        cv2.drawContours(frame, [approx5], -1, (203,192,255), 3)
        
        """
        if area5> 400:
            
            if len(approx5) == 3:
                cv2.putText(frame, "Triangle", (cX5+20, cY5+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
            elif len(approx5) == 4:
                cv2.putText(frame, "Rectangle", (cX5+20, cY5+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)    
            elif len(approx5) == 5:
                cv2.putText(frame, "Pentagon", (cX5+20, cY5+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
            elif len(approx5) == 6:
                cv2.putText(frame, "Hexagon", (cX5+20, cY5+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
            elif len(approx5) == 10:
                cv2.putText(frame, "Star", (cX5+20, cY5+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)                    
            else:
                cv2.putText(frame, "Circle", (cX5+20, cY5+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)                           
        """    
    for cnt6 in cont6:
        
        area6 = cv2.contourArea(cnt6)
        approx6 = cv2.approxPolyDP(cnt6, 0.02*cv2.arcLength(cnt6,True), True)
        M6 = cv2.moments(cnt6)
        cX6 = int(M6["m10"]/M6["m00"])
        cY6 = int (M6["m01"]/M6["m00"])
        #cv2.putText(frame, "Brown", (cX6-20,cY6-20),cv2.FONT_HERSHEY_COMPLEX, 1, (30, 101, 181), 2)
        #cv2.circle(frame, (cX6, cY6), 7, (30, 101, 181), -1)
        cv2.drawContours(frame, [approx6], -1, (30, 101, 181), 3)
        
        """
        if area6> 400:
            
            if len(approx6) == 3:
                cv2.putText(frame, "Triangle", (cX6+20, cY6+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
            elif len(approx6) == 4:
                cv2.putText(frame, "Rectangle", (cX6+20, cY6+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)    
            elif len(approx6) == 5:
                cv2.putText(frame, "Pentagon", (cX6+20, cY6+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
            elif len(approx6) == 6:
                cv2.putText(frame, "Hexagon", (cX6+20, cY6+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
            elif len(approx6) == 10:
                cv2.putText(frame, "Star", (cX6+20, cY6+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)                    
            else:
                cv2.putText(frame, "Circle", (cX6+20, cY6+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)               
        """
    for cnt7 in cont7:
        
        area7 = cv2.contourArea(cnt7)
        approx7 = cv2.approxPolyDP(cnt7, 0.02*cv2.arcLength(cnt7,True), True)
        M7 = cv2.moments(cnt7)
        cX7 = int(M7["m10"]/M7["m00"])
        cY7 = int (M7["m01"]/M7["m00"])
        #cv2.putText(frame, "Orange", (cX7-20,cY7-20),cv2.FONT_HERSHEY_COMPLEX, 1, (0,165,255), 2)
        #cv2.circle(frame, (cX7, cY7), 7, (0,165,255), -1)
        cv2.drawContours(frame, [approx7], -1, (0,165,255), 3)
        
        """
        if area7> 400:
            
            if len(approx7) == 3:
                cv2.putText(frame, "Triangle", (cX7+20, cY7+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
            elif len(approx7) == 4:
                cv2.putText(frame, "Rectangle", (cX7+20, cY7+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)    
            elif len(approx7) == 5:
                cv2.putText(frame, "Pentagon", (cX7+20, cY7+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
            elif len(approx7) == 6:
                cv2.putText(frame, "Hexagon", (cX7+20, cY7+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
            elif len(approx7) == 10:
                cv2.putText(frame, "Star", (cX7+20, cY7+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)                    
            else:
                cv2.putText(frame, "Circle", (cX7+20, cY7+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)             
        """
    for cnt8 in cont8:
        
        area8 = cv2.contourArea(cnt8)
        approx8 = cv2.approxPolyDP(cnt8, 0.02*cv2.arcLength(cnt8,True), True)
        M8 = cv2.moments(cnt8)
        cX8 = int(M8["m10"]/M8["m00"])
        cY8 = int (M8["m01"]/M8["m00"])
        #cv2.putText(frame, "White", (cX8-20,cY8-20),cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
        #cv2.circle(frame, (cX8, cY8), 7, (255,255,255), -1)
        cv2.drawContours(frame, [approx8], -1, (255,255,255), 3)
        
        """
        if area8> 400:
            
            if len(approx8) == 3:
                cv2.putText(frame, "Triangle", (cX8+20, cY8+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
            elif len(approx8) == 4:
                cv2.putText(frame, "Rectangle", (cX8+20, cY8+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)    
            elif len(approx8) == 5:
                cv2.putText(frame, "Pentagon", (cX8+20, cY8+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
            elif len(approx8) == 6:
                cv2.putText(frame, "Hexagon", (cX8+20, cY8+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
            elif len(approx8) == 10:
                cv2.putText(frame, "Star", (cX8+20, cY8+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)                    
            else:
                cv2.putText(frame, "Circle", (cX8+20, cY8+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)             
        """
    for cnt9 in cont9:
        
        area9 = cv2.contourArea(cnt9)
        approx9 = cv2.approxPolyDP(cnt9, 0.02*cv2.arcLength(cnt9,True), True)
        M9 = cv2.moments(cnt9)
        cX9 = int(M9["m10"]/M9["m00"])
        cY9 = int (M9["m01"]/M9["m00"])
        #cv2.putText(frame, "Purple", (cX9-20,cY9-20),cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,143), 2)
        #cv2.circle(frame, (cX9, cY9), 7, (255,0,143), -1)
        cv2.drawContours(frame, [approx9], -1, (255,0,143), 3)
        
        """
        if area9> 400:
            
            if len(approx9) == 3:
                cv2.putText(frame, "Triangle", (cX9+20, cY9+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
            elif len(approx9) == 4:
                cv2.putText(frame, "Rectangle", (cX9+20, cY9+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)    
            elif len(approx9) == 5:
                cv2.putText(frame, "Pentagon", (cX9+20, cY9+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
            elif len(approx9) == 6:
                cv2.putText(frame, "Hexagon", (cX9+20, cY9+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
            elif len(approx9) == 10:
                cv2.putText(frame, "Star", (cX9+20, cY9+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)                    
            else:
                cv2.putText(frame, "Circle", (cX9+20, cY9+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)             
        """
    for cnt10 in cont10:
        
        area10 = cv2.contourArea(cnt10)
        approx10 = cv2.approxPolyDP(cnt10, 0.02*cv2.arcLength(cnt10,True), True)
        M10 = cv2.moments(cnt10)
        cX10 = int(M10["m10"]/M10["m00"])
        cY10 = int (M10["m01"]/M10["m00"])
        #cv2.putText(frame, "Gray", (cX10-20,cY10-20),cv2.FONT_HERSHEY_COMPLEX, 1, (128,128,128), 2)
        #cv2.circle(frame, (cX10, cY10), 7, (128,128,128), -1)
        cv2.drawContours(frame, [approx10], -1, (128,128,128), 3)
        
        """
        if area10> 400:
            
            if len(approx10) == 3:
                cv2.putText(frame, "Triangle", (cX10+20, cY10+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
            elif len(approx10) == 4:
                cv2.putText(frame, "Rectangle", (cX10+20, cY10+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)    
            elif len(approx10) == 5:
                cv2.putText(frame, "Pentagon", (cX10+20, cY10+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
            elif len(approx10) == 6:
                cv2.putText(frame, "Hexagon", (cX10+20, cY10+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
            elif len(approx10) == 10:
                cv2.putText(frame, "Star", (cX10+20, cY10+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)                    
            else:
                cv2.putText(frame, "Circle", (cX10+20, cY10+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)                                                   
        """
    for cnt11 in cont11:
        
        area11 = cv2.contourArea(cnt11)
        approx11 = cv2.approxPolyDP(cnt11, 0.02*cv2.arcLength(cnt11,True), True)
        M11 = cv2.moments(cnt11)
        cX11 = int(M11["m10"]/M11["m00"])
        cY11 = int (M11["m01"]/M11["m00"])
        #cv2.putText(frame, "Black", (cX11-20,cY11-20),cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,0), 2)
        #cv2.circle(frame, (cX11, cY11), 7, (0,0,0), -1)
        cv2.drawContours(frame, [approx11], -1, (0,0,0), 3)
        
        """
        if area11> 400:
            
            if len(approx11) == 3:
                cv2.putText(frame, "Triangle", (cX11+20, cY11+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
            elif len(approx11) == 4:
                cv2.putText(frame, "Rectangle", (cX11+20, cY11+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)    
            elif len(approx11) == 5:
                cv2.putText(frame, "Pentagon", (cX11+20, cY11+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
            elif len(approx11) == 6:
                cv2.putText(frame, "Hexagon", (cX11+20, cY11+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
            elif len(approx11) == 10:
                cv2.putText(frame, "Star", (cX11+20, cY11+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)                    
            else:
                cv2.putText(frame, "Circle", (cX11+20, cY11+20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)             
        """     
    cv2.imshow("Frame", frame)
    
    if cv2.waitKey(25) & 0xff == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
    
                 