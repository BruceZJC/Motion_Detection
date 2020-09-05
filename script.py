import cv2

img= cv2.imread("hired.jpeg",1)
print(img)
print(img.shape)

resized_image=cv2.resize(img,(500,500))
cv2.imshow("hire",resized_image)
cv2.waitKey(2000)
cv2.destroyAllWindows()