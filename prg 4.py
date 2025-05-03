import cv2 
import numpy as np 
image = cv2.imread("C:\\Users\\Hp 440 G10\\Downloads\\OIP.jpg")  # Replace with your image file 
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
equalized_image = cv2.equalizeHist(gray_image) 
cv2.imshow("Original Grayscale Image", gray_image) 
cv2.imshow("Histogram Equalized Image", equalized_image) 
cv2.waitKey(0) 
cv2.destroyAllWindows()        
