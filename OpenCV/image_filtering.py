# image filtering ->
# 1. blurring -> gaussin, median, bilateral, normal
# 2. noise
# 3. smoothing
# 4. kernel

# gaussian blur - image ko soft krna, removing noise, dust and sharp images, smoothing

# blurred_image = cv.GaussianBlur(image, (kernel_size_x, kernel_size_y))

# kernel size -(3,3)->light blur ; (9,9) -> strong blur; (21,21)-> super blur

'''
import cv2 
image = cv2.imread("envy.jpg")
blurred = cv2.GaussianBlur(image,(7,7), 0)

cv2.imshow("original image", image)
cv2.imshow("blurred image", blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

#median blur 
# blurred = cv2.medianBlur(image, kernel_size)

'''
import cv2
image = cv2.imread("envy.jpg")
blurred = cv2.medianBlur(image, 5)

cv2.imshow("original", image)
cv2.imshow("clean image", blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

# sharpening -> highlight the edges, pixel ke bich me jo contrast hota h usko boost kr deta h
# cv2.filter(src, depth, kernel)

'''
import cv2
import numpy as np

image = cv2.imread("low_res.jpg")

sharpen_kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

sharpened = cv2.filter2D(image, -1, sharpen_kernel)
cv2.imshow("original image", image)
cv2.imshow("sharpened image", sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

