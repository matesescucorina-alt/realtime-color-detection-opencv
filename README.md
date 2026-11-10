# Real-Time Color Recognition in Python and OpenCV

A real-time computer vision system capable of identifying, tracking, and localizing multiple objects across the entire visible spectrum using Python, OpenCV, and NumPy[cite: 3]. Developed as part of the Applied Informatics curriculum at the Politehnica University of Timișoara.

---

## Features
- **Broad Spectrum Tracking:** Detects 13 distinct color categories including challenging neutral tones (White, Black, Gray) and difficult hues[cite: 3, 7].
- **Dual-Threshold Red Detection:** Accounts for the circular "wrap-around" nature of Red in the HSV cylinder (spanning both 0° and 180° in OpenCV)[cite: 3, 5, 6].
- **High-Performance Pipeline:** Optimized with NumPy array pre-processing to ensure low-latency tracking at standard camera frame rates (30+ FPS)[cite: 3, 10].
- **Robust Segmentation:** Employs Gaussian Blur for noise reduction and morphological transformations (erosion and dilation) to clean binary masks and minimize false positives[cite: 3, 4, 9].

---

## The Image Processing Pipeline
1. **Stream Acquisition:** Captures live video frames via `cv2.VideoCapture(0)`[cite: 9].
2. **Noise Reduction:** Applies a Gaussian Blur filter to smooth out pixel variations and camera static[cite: 4, 9].
3. **Color Masking:** Converts frames from BGR to HSV color space and uses `cv2.inRange` to generate binary masks based on predefined threshold matrices[cite: 3, 4, 9].
4. **Morphological Filtering:** Executes erosion followed by dilation to eliminate speckles and fill gaps inside targeted objects[cite: 4, 9].
5. **Contour Analysis & Localization:** Detects object boundaries, filters out background noise using contour area thresholds, and draws real-time bounding boxes with class labels[cite: 3, 4, 6, 9].

---

## Color Segmentation Thresholds (HSV)

| Color Name | Lower HSV Boundary | Upper HSV Boundary | BGR Drawing Color |
| :--- | :--- | :--- | :--- |
| **Red (Lower)** | `[0, 120, 70]` | `[10, 255, 255]` | `(0, 0, 255)` |
| **Red (Upper)** | `[170, 120, 70]` | `[180, 255, 255]` | `(0, 0, 255)` |
| **Orange** | `[11, 150, 70]` | `[25, 255, 255]` | `(0, 165, 255)` |
| **Yellow** | `[26, 120, 70]` | `[35, 255, 255]` | `(0, 255, 255)` |
| **Green** | `[36, 50, 70]` | `[89, 255, 255]` | `(0, 255, 0)` |
| **Cyan** | `[90, 120, 70]` | `[105, 255, 255]` | `(255, 255, 0)` |
| **Blue** | `[106, 120, 70]` | `[129, 255, 255]` | `(255, 0, 0)` |
| **Purple** | `[130, 50, 70]` | `[150, 255, 255]` | `(128, 0, 128)` |
| **Magenta** | `[151, 120, 70]` | `[170, 255, 255]` | `(255, 0, 255)` |
| **Brown** | `[10, 100, 20]` | `[20, 255, 150]` | `(42, 42, 165)` |
| **White** | `[0, 0, 200]` | `[180, 30, 255]` | `(255, 255, 255)` |
| **Black** | `[0, 0, 0]` | `[180, 255, 40]` | `(50, 50, 50)` |
| **Gray** | `[0, 0, 40]` | `[180, 50, 200]` | `(128, 128, 128)` |

---

## Tech Stack
- **Language:** Python[cite: 3]
- **Libraries:** OpenCV (`cv2`), NumPy[cite: 3]

---

## Installation & Running

1. Clone the repository:
   ```bash
   git clone [https://github.com/matesescucorina-alt/realtime-color-detection-opencv.git](https://github.com/matesescucorina-alt/realtime-color-detection-opencv.git)
   cd realtime-color-detection-opencv
