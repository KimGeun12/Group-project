import cv2
import numpy as np


image = np.zeros((300, 400, 3), dtype=np.uint8)


cv2.circle(image, (100, 100), 50, (0, 0, 255), -1)


cv2.rectangle(image, (200, 50), (300, 150), (255, 0, 0), -1)

pts = np.array([[50, 200], [150, 200], [100, 300]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.polylines(image, [pts], True, (0, 255, 0), thickness=3)

cv2.imwrite('Example02_image_result.png', image)


cv2.imshow('Shapes', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
