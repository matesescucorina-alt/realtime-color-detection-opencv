# -*- coding: utf-8 -*-
"""
Created on Thu May 14 11:20:44 2026

@author: HP
"""

import cv2
import numpy as np


cap = cv2.VideoCapture(0)


# HSV Ranges: [Lower], [Upper], (BGR Color for Drawing)
color_map = {
    "Red": ([0, 120, 70], [10, 255, 255], (0, 0, 255)),
    "Orange": ([11, 120, 70], [25, 255, 255], (0, 165, 255)),
    "Yellow": ([26, 120, 70], [35, 255, 255], (0, 255, 255)),
    "Green": ([36, 50, 70], [89, 255, 255], (0, 255, 0)),
    "Cyan": ([90, 120, 70], [105, 255, 255], (255, 255, 0)),
    "Blue": ([106, 120, 70], [129, 255, 255], (255, 0, 0)),
    "Purple": ([130, 50, 70], [150, 255, 255], (128, 0, 128)),
    "Magenta": ([151, 120, 70], [170, 255, 255], (255, 0, 255))
}

while True:
    _, frame = cap.read()
    #  blur 
    blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)
    hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)

    for name, (lower, upper, bgr) in color_map.items():
        lower_arr = np.array(lower)
        upper_arr = np.array(upper)

        # mask
        mask = cv2.inRange(hsv, lower_arr, upper_arr)
        
        # Clean mask 
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
            if cv2.contourArea(cnt) > 1000:
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(frame, (x, y), (x + w, y + h), bgr, 2)
                cv2.putText(frame, name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, bgr, 2)

    cv2.imshow("Advanced Multi-Color Detector", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()