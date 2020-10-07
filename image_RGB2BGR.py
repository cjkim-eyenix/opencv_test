import cv2

rgb_image = cv2.imread('Lenna.png')
bgr_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2BGR)

cv2.imshow('rgb_image', rgb_image)
cv2.imshow('bgr_image', bgr_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
