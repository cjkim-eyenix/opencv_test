import cv2

rgb_image = cv2.imread('Lenna.png')

resize_image = cv2.resize(rgb_image, (300,300))

cv2.imshow('rgb_image', rgb_image)
cv2.imshow('resize_image', resize_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
