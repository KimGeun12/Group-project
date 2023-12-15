# 프로젝트 이름: BlurFrameSketcher

## 1. 프로젝트 개요:  
openCV의 가장 기초적인 이미지 전처리와 도형 그리기 기능을 활용하여 원본 이미지를 블러 처리한 후, 블러 처리된 이미지에서 테두리를 찾아 그려내도록 하는 프로그램 제작  
- 프로그램 실행 과정(순서): 원본 이미지 불러오기-> 원본 이미지 블러 처리 -> 블러 처리된 이미지의 그림 위에 테두리를 그려냄 -> 3가지 이미지 파일 동시에 출력
- Example01, Example02 코드를 통해 최종 프로젝트 코드에 활용될 명령어들의 사용 예시를 나타냄


# 2. BlurFrameSketcher 코드 설명 및 결과

## (1) 라이브러리 가져오기

```python
import cv2
import numpy as np
```
OpenCV 라이브러리 (cv2): 이미지 처리를 위해 사용됨
NumPy 라이브러리 (np): 숫자 연산에 사용됨

## (2) 함수 정의

```python
def combine_blurred_and_contoured(image_path, blur_amount=(25, 25), canny_threshold1=50,canny_threshold2=100):
```
이미지 파일 경로 (image_path)를 받음
블러 (blur_amount) 및 프레임 감지 임계값 (canny_threshold1 및 canny_threshold2)을 설정

## (3) 이미지 로드 및 변환

```python
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
```
컬러 이미지를 그레이스케일로 변환하여 처리 단순화

## (4) 블러 적용 및 엣지 검출

```python
blurred = cv2.GaussianBlur(gray, blur_amount, 0)
edges = cv2.Canny(blurred, canny_threshold1, canny_threshold2)
```
그레이스케일 이미지에 블러 적용
Canny 프레임 검출을 사용하여 블러된 이미지에서 프레임을 식별

## (5) 등고선 찾기 및 블러처리된 이미지에 그리기

```python
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contoured_image = cv2.cvtColor(blurred, cv2.COLOR_GRAY2BGR)
cv2.drawContours(contoured_image, contours, -1, (255, 0, 0), 3)
```
OpenCV의 findContours 함수를 사용하여 프레임이 감지된 이미지에서 등고선을 찾음

## (6) 이미지 결합 및 저장
```python
combined = np.hstack((image, cv2.cvtColor(blurred, cv2.COLOR_GRAY2BGR), contoured_image))
combined_image_path = 'C://Users//User//Desktop//combined_image.jpg'
cv2.imwrite(combined_image_path, combined)
```
원본 이미지, 블러된 이미지 및 등고선 결합 

## (7) 결과

#### 원본
<img src="https://github.com/KimGeun12/TermProject-BlurFrameSketcher/blob/main/image.jpg" width="400" height="400"/>

#### 블러처리 
![블러처리](https://github.com/KimGeun12/TermProject-BlurFrameSketcher/blob/main/Example01_image_result.jpg)

#### 그레이스케일 변환 및 프레임 검출(프로젝트의 최종 결과)
![그레이스케일 변환 및 프레임 검출](https://github.com/KimGeun12/TermProject-BlurFrameSketcher/blob/main/Project_image.jpg)

## 3. 사용 패키지: 
- opencv(4.8.1)  
- pyhon(3.11.5)  
- numpy(1.24.4)  

## 4. 실행방법:
원본이미지(가천대로고)를 다운로드 한 뒤, 코드에 해당 이미지 파일의 경로를 정확하게 작성 후 visual studio code에서 프로그램 실행

## 5. 참고자료 및 출처
- https://www.youtube.com/watch?v=lelVripbt2M 
- <br> https://github.com/jIdle/GaussianBlur-CUDA
- <br> https://docs.opencv.org/4.x/dc/da5/tutorial_py_drawing_functions.html
- <br> https://learnopencv.com/contour-detection-using-opencv-python-c/  
