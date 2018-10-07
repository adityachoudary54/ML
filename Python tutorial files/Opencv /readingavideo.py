#Read a Video Stream from Camera(Frame by frame)
import cv2
cap=cv2.VideoCapture(0)

while True:
	ret,frame=cap.read()
	gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	if ret==False:
		continue
	cv2.imshow("Video frame",frame)
	cv2.imshow("Gray frame",gray_frame)
	#wait for user input-q then u will stop the loop
	key_pressed=cv2.waitKey(1) & 0xFF#here we convert a 32 bit no. to 8 bit no.
	if key_pressed == ord('q'):#here the comparision is made
		break
cap.release()
cv2.destroyAllWindows()
