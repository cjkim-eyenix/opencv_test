import cv2

rgb_image = cv2.imread('Lenna.png')

crop_image = rgb_image.copy()
crop_image = rgb_image[50:600, 100:700]

cv2.imshow('rgb_image', rgb_image)
cv2.imshow('crop_image', crop_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
