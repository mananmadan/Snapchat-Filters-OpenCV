import numpy as np
import cv2 
import matplotlib.pyplot as plt
glasses = cv2.imread('experimental/glasses.jpg')
moustache = cv2.imread('experimental/moustache-2.jpg')
mydict = {}
name_list = [
'left_eye_center_x',
'left_eye_center_y',
'right_eye_center_x',
'right_eye_center_y',
'left_eye_inner_corner_x',
'left_eye_inner_corner_y',
'left_eye_outer_corner_x',
'left_eye_outer_corner_y',
'right_eye_inner_corner_x',
'right_eye_inner_corner_y',
'right_eye_outer_corner_x',
'right_eye_outer_corner_y',
'left_eyebrow_inner_end_x',
'left_eyebrow_inner_end_y',
'left_eyebrow_outer_end_x',
'left_eyebrow_outer_end_y',
'right_eyebrow_inner_end_x',
'right_eyebrow_inner_end_y',
'right_eyebrow_outer_end_x',
'right_eyebrow_outer_end_y',
'nose_tip_x',
'nose_tip_y',
'mouth_left_corner_x',
'mouth_left_corner_y',
'mouth_right_corner_x',
'mouth_right_corner_y',
'mouth_center_top_lip_x',
'mouth_center_top_lip_y',
'mouth_center_bottom_lip_x',
'mouth_center_bottom_lip_y']

def make_dict(label_points):
    for i in range(0,len(name_list)):
      mydict[name_list[i]] = label_points[0][i]
  

def filtering(label_points,types):
    make_dict(label_points)
    if types == 'glasses':
      return [(mydict['left_eyebrow_outer_end_x'],mydict['left_eyebrow_outer_end_y']),(mydict['right_eyebrow_outer_end_x'],mydict['right_eyebrow_outer_end_y'])]
        
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
    if types == 'glasses':
        global glasses
        #print("in glasses")
        x1,y1 = points[0]
        x2,y2 = points[1]
        x1 = int(x1)
        x2 = int(x2)
        y = int((y1+y2)/2)
        #print(x1,x2,y)
        y = y-5
        temp = cv2.resize(glasses,((x1-x2)+10,30))
        for i in range(0,temp.shape[0]):
          for j in range(0,temp.shape[1]):
            r,g,b = temp[i,j,:]
            if r<180 or g<180 or b<180:
              img[y+i,j+(x2-5),:] = r,g,b

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
        cv2.addweighted(overlay,opacity,img,1-opacity,0,img)
    if types == 'moustache':
        x = int(points[0])
        y = int(points[1])
        for i in range(0,min(29,96-y)):
            for j in range(0,90):
               b,g,r = moustache[i][j][:]
               if b<215 or g<215 or r<215:
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
        h = int(img.shape[1])
        w = int(img.shape[0])
        hat_img = cv2.imread('filters/hat.jpg')
        #img_o = img[0:w,he:h,:]
        hat_img = cv2.resize(hat_img,(w,h))
        print(x-nx,x+(w-nx),y-(h-he),y)
        img_h = hat_img[x-nx:x+(w-nx),y-(h-he):y,:]
        cv2.imshow('wind',img_h)
        cv2.waitkey(0)
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
