import numpy as np
import cv2 
import matplotlib.pyplot as plt
moustache = cv2.imread('experimental/moustache.jpg')
def filtering(label_points,types):
    if types == 'gogles':
        centre_left = (int((label_points[0][0] + label_points[0][6]) / 2) , int((label_points[0][1] + label_points[0][7]) / 2))
        centre_right = (int((label_points[0][2] + label_points[0][10]) /2) , int((label_points[0][3] + label_points[0][11])/2))
        left_radius = int(abs(centre_left[0] - label_points[0][12])) 
        right_radius = int(abs(centre_right[0]- label_points[0][18]))
        max_radius =  max(left_radius,right_radius)
        left_radius = right_radius = max_radius
        length_start = (label_points[0][12],label_points[0][13])
        length_end = (label_points[0][16],label_points[0][17])
        ll = [centre_left,left_radius,centre_right,right_radius,length_start,length_end]
        return ll
    if types == 'moustache':
        ## we want the hat to be place in the region at the height of eyebrows + 10
        ll = [label_points[0][20],label_points[0][21]]
        return ll
          
def apply(img,points,types):
    if types == 'gogles':
        centre_left = points[0]
        centre_l_radius = points[1]
        centre_right = points[2]
        centre_r_radius = points[3]
        length_start = points[4]
        length_end = points[5]
        overlay = img.copy()
        cv2.circle(overlay,centre_left,int(centre_l_radius),(0,0,0),-1)
        cv2.circle(overlay,centre_left,int(centre_l_radius),(192,192,192),1)
        cv2.circle(overlay,centre_right,int(centre_r_radius),(0,0,0),-1)
        cv2.circle(overlay,centre_right,int(centre_r_radius),(192,192,192),1)
        cv2.line(overlay,(centre_left[0]-int(centre_l_radius),length_start[1]),(centre_right[0]+int(centre_r_radius),length_end[1]),(192,192,192),2)
        opacity = 0.6
        cv2.addWeighted(overlay,opacity,img,1-opacity,0,img)
    if types == 'moustache':
        x = int(points[0])
        y = int(points[1])
        for i in range(0,min(29,96-y)):
            for j in range(0,90):
               b,g,r = moustache[i][j][:]
               if b<235 or g<235 or r<235:
                 try:
                   img[y+i][j+(x-45)][:] = r,g,b 
                 except:
                   print("out of bounds")


    '''
    if types == 'hat':
        he = int(points[0])
        nx = int(points[1])
        x  = 200
        y = 400
        H = int(img.shape[1])
        W = int(img.shape[0])
        hat_img = cv2.imread('filters/hat.jpg')
        #img_o = img[0:W,he:H,:]
        hat_img = cv2.resize(hat_img,(W,H))
        print(x-nx,x+(W-nx),y-(H-he),y)
        img_h = hat_img[x-nx:x+(W-nx),y-(H-he):y,:]
        cv2.imshow('wind',img_h)
        cv2.waitKey(0)
        for i in range(0,img_h.shape[0]):
            for j in range(0,img_h.shape[1]):
               r,g,b = img_h[i][j][:]
               if r<235 or g<235 or b<235:
                 try:
                   img[i][j+he][:] = r,g,b
                 except:
                   print("out of bounds")
    '''
    ''' 
    if types == 'hat':
         x = points[0] / 450
         image_width = img.shape[0]
         image_height = int(hat_img.shape[0] * x)
         hat_img = cv2.resize(hat_img,(int(image_width),int(image_height)))
         
         for i in range(0,hat_img.shape[0]):
             for j in range(0,hat_img.shape[1]):
                 r,g,b = hat_img[i][j][:]
                 if r<235 or g<235 or b<235:
                   try:
                    img[i][j][:] = (r,g,b)
                   except:
                     print("out of bounds")
        
    '''
    return img
