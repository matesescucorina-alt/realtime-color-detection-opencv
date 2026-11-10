# -*- coding: utf-8 -*-
"""
Created on Thu May 28 12:23:06 2026

@author: HP
"""

import cv2
import numpy as np
import sys
import os

# --- COLOR CONFIGURATION ---
# "Name": [Lower_HSV, Upper_HSV, BGR_Drawing_Color]
COLOR_DICT = {
    "Red": [np.array([0, 120, 70]), np.array([10, 255, 255]), (0, 0, 255)],
    "Green": [np.array([35, 100, 100]), np.array([85, 255, 255]), (0, 255, 0)],
    "Blue": [np.array([100, 150, 0]), np.array([140, 255, 255]), (255, 0, 0)],
    "Yellow": [np.array([20, 100, 100]), np.array([30, 255, 255]), (0, 255, 255)]
}

def process_frame(frame):
    """Core logic to detect colors in a single frame/image."""
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    for name, (lower, upper, draw_color) in COLOR_DICT.items():
        mask = cv2.inRange(hsv, lower, upper)
        # Clean up noise with Morphology
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)
        
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        for cnt in contours:
            if cv2.contourArea(cnt) > 500:
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(frame, (x, y), (x + w, y + h), draw_color, 2)
                cv2.putText(frame, name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, draw_color, 2)
    return frame

def main():
    # Check if a file path was passed as an argument
    # Usage: python script.py image.jpg
    source = 0
    if len(sys.argv) > 1:
        source = sys.argv[1]

    if isinstance(source, str) and os.path.exists(source):
        # PROCESS IMAGE
        print(f"Processing image: {source}")
        img = cv2.imread(source)
        result = process_frame(img)
        cv2.imshow('Color Detection - Image', result)
        cv2.waitKey(0) # Wait until a key is pressed
    else:
        # PROCESS WEBCAM
        print("No image provided or file not found. Starting Webcam...")
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            if not ret: break
            
            result = process_frame(frame)
            cv2.imshow('Color Detection - Webcam', result)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()