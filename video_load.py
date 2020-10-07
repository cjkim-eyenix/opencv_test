import cv2

cap = cv2.VideoCapture('Creux De Van - 45150.mp4')

while True:
	ret, frame = cap.read()

	if ret == False:
		break

	cv2.imshow("Color_video", frame)

	if cv2.waitKey(1) & 0xFF == 27:
		break 
cap.release()
cv2.destroyAllWindows()
