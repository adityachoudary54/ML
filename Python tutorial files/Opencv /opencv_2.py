import cv2
img=cv2.imread("2017-Ford-Mustang-Shelby-GT350-01-placement.jpg")
gray=cv2.imread("2017-Ford-Mustang-Shelby-GT350-01-placement.jpg",cv2.IMREAD_GRAYSCALE)
x=img.shape[0]
y=img.shape[1]
img=cv2.resize(img,(int(y/4),int(x/4)))
gray=cv2.resize(gray,(int(y/4),int(x/4)))
cv2.imshow("Mustang",img)
cv2.imshow("Mustang greyish",gray)
cv2.waitKey(0)# 0 means wait for infinite amount of time
cv2.destroyAllWindows()
