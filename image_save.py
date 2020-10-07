import cv2

rgb_image = cv2.imread('Lenna.png')
gray_image = cv2.imread('Lenna.png', 0)

cv2.imwrite('/home/cjkim/opencv_test/image_save_folder/gray_image.jpg', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
