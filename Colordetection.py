# -*- coding: utf-8 -*-



import cv2
import numpy as np

cap = cv2.VideoCapture(0)



color_map = {
    "Red (Lower)": ([0, 120, 70], [10, 255, 255], (0, 0, 255)),
    "Red (Upper)": ([170, 120, 70], [180, 255, 255], (0, 0, 255)),
    "Orange": ([11, 150, 70], [25, 255, 255], (0, 165, 255)),
    "Yellow": ([26, 120, 70], [35, 255, 255], (0, 255, 255)),
    "Green": ([36, 50, 70], [89, 255, 255], (0, 255, 0)),
    "Cyan": ([90, 120, 70], [105, 255, 255], (255, 255, 0)),
    "Blue": ([106, 120, 70], [129, 255, 255], (255, 0, 0)),
    "Purple": ([130, 50, 70], [150, 255, 255], (128, 0, 128)),
    "Magenta": ([151, 120, 70], [170, 255, 255], (255, 0, 255)),
    "Brown": ([10, 100, 20], [20, 255, 150], (42, 42, 165)),
    "White": ([0, 0, 200], [180, 30, 255], (255, 255, 255)),
    "Black": ([0, 0, 0], [180, 255, 40], (50, 50, 50)), 
    "Gray": ([0, 0, 40], [180, 50, 200], (128, 128, 128))
}


processed_colors = []
for name, (low, high, bgr) in color_map.items():
    processed_colors.append((name, np.array(low), np.array(high), bgr))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Blur 
    blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)
    hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)

    for name, lower_arr, upper_arr, bgr in processed_colors:
        # Create mask
        mask = cv2.inRange(hsv, lower_arr, upper_arr)
        
        # Clean mask (Erode/Dilate)
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
            if cv2.contourArea(cnt) > 1500: # Filter more noise
                x, y, w, h = cv2.boundingRect(cnt)
                
                
                display_name = "Red" if "Red" in name else name
                
                cv2.rectangle(frame, (x, y), (x + w, y + h), bgr, 2)
                cv2.putText(frame, display_name, (x, y - 10), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, bgr, 2)

    cv2.imshow("Super Multi-Color Detector", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

