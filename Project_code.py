import cv2
import numpy as np

def combine_blurred_and_contoured(image_path, blur_amount=(25, 25), canny_threshold1=50, canny_threshold2=100):
    # Load the image
    image = cv2.imread(image_path)
    
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(gray, blur_amount, 0)
    
    # Find edges using Canny
    edges = cv2.Canny(blurred, canny_threshold1, canny_threshold2)
    
    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Draw contours on a copy of the blurred image
    contoured_image = cv2.cvtColor(blurred, cv2.COLOR_GRAY2BGR)
    cv2.drawContours(contoured_image, contours, -1, (255, 0, 0), 3) 
    
    # Combine the images side by side
    combined = np.hstack((image, cv2.cvtColor(blurred, cv2.COLOR_GRAY2BGR), contoured_image))
    
    return combined

image_path = 'C://Users//User//Desktop//image//image.jpg'

combined_image = combine_blurred_and_contoured(image_path)

combined_image_path = 'C://Users//User//Desktop//combined_image.jpg'
cv2.imwrite(combined_image_path, combined_image)

print("Image saved at:", combined_image_path)