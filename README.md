# Project Name: BlurFrameSketcher

## 1. Project Overview: 
Create a program that uses basic image preprocessing and shape drawing features of OpenCV to blur an original image, and then find and draw the edges on the blurred image  
- Program Execution Process (Order): Load original image -> Blur the original image -> Draw edges on the blurred image -> Display all three image files simultaneously
- Example01, Example02 codes demonstrate the use of commands that will be utilized in the final project code.


# 2. BlurFrameSketcher Code Description and Results

## (1) Import Libraries

```python
import cv2
import numpy as np
```
- OpenCV library (cv2): Used for image processing
- NumPy library (np): Used for numerical operations

## (2) Function Definition

```python
def combine_blurred_and_contoured(image_path, blur_amount=(25, 25), canny_threshold1=50,canny_threshold2=100):
```
- Receives the image file path (image_path)
- Sets the blur amount (blur_amount) and frame detection thresholds (canny_threshold1 and canny_threshold2)

## (3) Image Loading and Conversion

```python
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
```
- Simplify processing by converting color images to grayscale

## (4) Apply Blur and Detect Edges

```python
blurred = cv2.GaussianBlur(gray, blur_amount, 0)
edges = cv2.Canny(blurred, canny_threshold1, canny_threshold2)
```
- Apply blur to the grayscale image
- Use **Canny edge detection** to identify frames in the blurred image

## (5) Find Contours and Draw on the Blurred Image

```python
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contoured_image = cv2.cvtColor(blurred, cv2.COLOR_GRAY2BGR)
cv2.drawContours(contoured_image, contours, -1, (255, 0, 0), 3)
```
- Use OpenCV's **findContours function** to find contours in the image where edges have been detected.

## (6) Image combining and saving
```python
combined = np.hstack((image, cv2.cvtColor(blurred, cv2.COLOR_GRAY2BGR), contoured_image))
combined_image_path = 'C://Users//User//Desktop//combined_image.jpg'
cv2.imwrite(combined_image_path, combined)
```
- Combining original image, blurred image, and contour lines

## (7) Resultant image

#### Original Image
<img src="https://github.com/KimGeun12/TermProject-BlurFrameSketcher/blob/main/image.jpg" width="400" height="400"/>

#### Blurred image
![블러처리](https://github.com/KimGeun12/TermProject-BlurFrameSketcher/blob/main/Example01_image_result.jpg)

#### Grayscale conversion and frame detection image (final result of the project)
![그레이스케일 변환 및 프레임 검출](https://github.com/KimGeun12/TermProject-BlurFrameSketcher/blob/main/Project_image.jpg)

## 3. Used packages:
- opencv(4.8.1)  
- pyhon(3.11.5)  
- numpy(1.24.4)  

## 4. Method of running the program:
After downloading the original image(가천대 로고), write the exact path of the image file and the download location in the code, then run the program in Visual Studio Code

## 5. References and sources
- https://www.youtube.com/watch?v=lelVripbt2M
- https://github.com/jIdle/GaussianBlur-CUDA
- https://docs.opencv.org/4.x/dc/da5/tutorial_py_drawing_functions.html
- https://learnopencv.com/contour-detection-using-opencv-python-c/
