# 블러프레임스케처 코드 설명

## 1. 라이브러리 가져오기

```python
import cv2
import numpy as np
```
OpenCV 라이브러리 (cv2): 이미지 처리를 위해 사용됨
NumPy 라이브러리 (np): 숫자 연산에 사용됨

## 2. 함수 정의

```python
def combine_blurred_and_contoured(image_path, blur_amount=(25, 25), canny_threshold1=50,canny_threshold2=100):
```
이미지 파일 경로 (image_path)를 받음
블러 (blur_amount) 및 프레임 감지 임계값 (canny_threshold1 및 canny_threshold2)을 설정

## 3. 이미지 로드 및 변환

```python
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
```
컬러 이미지를 그레이스케일로 변환하여 처리 단순화

## 4. 블러 적용 및 엣지 검출

```python
blurred = cv2.GaussianBlur(gray, blur_amount, 0)
edges = cv2.Canny(blurred, canny_threshold1, canny_threshold2)
```
그레이스케일 이미지에 블러 적용
Canny 프레임 검출을 사용하여 블러된 이미지에서 프레임을을 식별

## 5. 등고선 찾기 및 블러처리된 이미지에 그리기

```python
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contoured_image = cv2.cvtColor(blurred, cv2.COLOR_GRAY2BGR)
cv2.drawContours(contoured_image, contours, -1, (255, 0, 0), 3)
```
OpenCV의 findContours 함수를 사용하여 프레임이 감지된 이미지에서 등고선을 찾음

## 6. 이미지 결합 및 저장
```python
combined = np.hstack((image, cv2.cvtColor(blurred, cv2.COLOR_GRAY2BGR), contoured_image))
combined_image_path = 'C://Users//User//Desktop//combined_image.jpg'
cv2.imwrite(combined_image_path, combined)
```
원본 이미지, 블러된 이미지 및 등고선합

# 결과



![Example01_image_result.jpg](https://github.com/KimGeun12/TermProject-BlurFrameSketcher/blob/main/Example01_image_result.jpg)

![Example01_image_result.jpg](https://github.com/KimGeun12/TermProject-BlurFrameSketcher/blob/main/Project_image.jpg)
