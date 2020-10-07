import cv2

gray_image = cv2.imread('Lenna.png', 0)

image_sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
image_sobel_x = cv2.convertScaleAbs(image_sobel_x)

image_sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
image_sobel_y = cv2.convertScaleAbs(image_sobel_y)

image_sobel = cv2.addWeighted(image_sobel_x, 1, image_sobel_y, 1, 0)

cv2.imshow('Sobel X', image_sobel_x)
cv2.imshow('Sobel Y', image_sobel_y)
cv2.imshow('Sobel', image_sobel)

cv2.waitKey(0)
cv2.destroyAllWindows()
