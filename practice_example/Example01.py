import numpy as np
import cv2

ori = cv2.imread('C:\\Users\\User\\Desktop\\image\\image.jpg', cv2.IMREAD_COLOR)

ori_blur = cv2.blur(ori, (20, 20))

resize_ori = cv2.resize(ori, (300, 300))
resize_ori_blur = cv2.resize(ori_blur, (300, 300))

compare_src = np.hstack((resize_ori, resize_ori_blur))

cv2.imshow('Image', compare_src)

cv2.waitKey(0)
cv2.destroyAllWindows()