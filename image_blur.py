import cv2

rgb_image = cv2.imread('Lenna.png')
blur_image = cv2.blur(rgb_image, (5,5))

cv2.imshow('rgb_image', rgb_image)
cv2.imshow('blur_image', blur_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
