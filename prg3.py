import cv2
image=cv2.imread("C:\\Users\\Hp 440 G10\\Downloads\\OIP.jpg")
gray_image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges=cv2.Canny(gray_image, 100,200)
cv2.imshow("original image",image)
cv2.imshow("edge detected image", edges)
cv2.waitkey(0)
cv2.destroyAllWindows()
