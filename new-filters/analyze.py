import cv2
img = cv2.imread('glasses-2.jpg')
img = cv2.resize(img,(200,30))
cv2.imwrite('glasses-2.jpg',img)
print(img.shape)