import numpy as np
import cv2 

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
    return img