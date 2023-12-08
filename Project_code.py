import cv2
import numpy as np

image_path = 'C:\\Users\\User\\Desktop\\image\\image.jpg'
image = cv2.imread(image_path)

if image is None:
    print("Error: 이미지를 불러오는 데 실패했습니다. 경로를 확인해 주세요.")
else:
    # Flip the image horizontally
    flipped_image = cv2.flip(image, 1)

    # Convert to grayscale and apply edge detection
    gray = cv2.cvtColor(flipped_image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)

    # Find contours from the edges
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Create an image to draw thick contours
    contour_image = np.zeros_like(flipped_image)

    # Draw the contours on the image with a certain thickness
    cv2.drawContours(contour_image, contours, -1, (255, 255, 255), thickness=3)

    # Save the result
    contour_image_path = 'C:\\Users\\User\\Desktop\\image\\contour_image.jpg'
    success = cv2.imwrite(contour_image_path, contour_image)

    if success:
        print("도형의 두꺼운 테두리가 그려진 이미지가 저장되었습니다:", contour_image_path)
    else:
        print("이미지 저장에 실패했습니다. 다시 시도해 주세요.")