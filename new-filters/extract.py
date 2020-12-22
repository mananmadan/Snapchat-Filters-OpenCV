## get-hat
import cv2
img_hat = cv2.imread('glasses-3.jpg')
#img_hat = cv2.resize(img_hat , (480,640))
img2 = img_hat.copy()
min_x = 3000
min_y = 3000
max_x = 0
max_y = 0
for i in range(0,img_hat.shape[0]):
  for j in range(0,img_hat.shape[1]):
     r,g,b = img_hat[i][j][:]
     if r<235 or g<235 or b<235:
        img2[i][j][:] = r,g,b
        min_x = min(min_x,i)
        min_y = min(min_y,j)
        max_x = max(max_x,i)
        max_y = max(max_y,j)
img2 = img2[min_x:max_x,min_y:max_y,:]
cv2.imwrite('glasses-2.jpg',img2)
