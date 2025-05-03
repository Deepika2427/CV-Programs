import cv2 
image = cv2.imread("C:\\Users\\Hp 440 G10\\Downloads\\OIP.jpg")  # Replace 'sample.jpg' with your image path 
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
cv2.imshow("Original Image", image) 
cv2.imshow("Grayscale Image", gray_image) 
cv2.waitKey(0) 
cv2.destroyAllWindows()
