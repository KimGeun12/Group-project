import cv2
import numpy as np

# Load the original image
image_path = 'C:\\Users\\User\\Desktop\image\\image.jpg'
image = cv2.imread(image_path)

# Check if the image is loaded properly
if image is None:
    print("Error: 이미지를 불러오는 데 실패했습니다. 경로를 확인해 주세요.")
else:
    # Convert to grayscale and apply edge detection
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)

    # Dilate the edges to make them thicker
    kernel = np.ones((5,5), np.uint8)  # Adjust kernel size for thickness
    dilated_edges = cv2.dilate(edges, kernel, iterations=1)

    # Create an image to draw thick colored contours
    thick_contour_image = np.zeros_like(image)

    # Extract colors from the original image where thick edges are found
    thick_contour_image[dilated_edges != 0] = image[dilated_edges != 0]

    # Save the result
    thick_contour_image_path = 'C:\\Users\\User\\Desktop\\main\\image_thick_contours.jpg'
    cv2.imwrite(thick_contour_image_path, thick_contour_image)

    print("색깔이 반영된 두꺼운 테두리가 그려진 이미지가 저장되었습니다:", thick_contour_image_path)
