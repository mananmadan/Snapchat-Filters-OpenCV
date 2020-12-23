import cv2
import time
import numpy as np

# load the filters
glasses = cv2.imread('filters/glasses-2.jpg')
moustache = cv2.imread('filters/moustache-2.jpg')

# dictionary for the landmarks
mydict = {}
name_list = ['left_eye_center_x', 'left_eye_center_y', 'right_eye_center_x', 'right_eye_center_y', 'left_eye_inner_corner_x', 'left_eye_inner_corner_y', 'left_eye_outer_corner_x', 'left_eye_outer_corner_y', 'right_eye_inner_corner_x', 'right_eye_inner_corner_y', 'right_eye_outer_corner_x', 'right_eye_outer_corner_y', 'left_eyebrow_inner_end_x', 'left_eyebrow_inner_end_y', 'left_eyebrow_outer_end_x', 'left_eyebrow_outer_end_y', 'right_eyebrow_inner_end_x', 'right_eyebrow_inner_end_y', 'right_eyebrow_outer_end_x', 'right_eyebrow_outer_end_y', 'nose_tip_x', 'nose_tip_y', 'mouth_left_corner_x', 'mouth_left_corner_y', 'mouth_right_corner_x', 'mouth_right_corner_y','mouth_center_top_lip_x', 'mouth_center_top_lip_y', 'mouth_center_bottom_lip_x','mouth_center_bottom_lip_y']

## load the dict
def make_dict(label_points):
    for i in range(0,len(name_list)):
      mydict[name_list[i]] = label_points[0][i]
  
## apply filters to the image using crazy maths!
def apply(img,points,types):
    make_dict(points)
    if 'glasses' in types.split(" "):
        global glasses
        x1,y1 = (mydict['left_eyebrow_outer_end_x'],mydict['left_eyebrow_outer_end_y'])
        x2,y2 = (mydict['right_eyebrow_outer_end_x'],mydict['right_eyebrow_outer_end_y'])
        x1 = int(x1)
        x2 = int(x2)
        y = int((y1+y2)/2)
        y = y-5
        temp = cv2.resize(glasses,((x1-x2)+10,30))

        ## apply glasses filter
        img[y:y+temp.shape[0],x2-5:temp.shape[1]+(x2-5),:] = np.where(temp<170,temp,img[y:y+temp.shape[0],x2-5:temp.shape[1]+(x2-5),:])

    if 'moustache' in types.split(" "):
        x = int(mydict['nose_tip_x'])
        y = int(mydict['nose_tip_y'])

        for i in range(0,min(29,96-y)):
            for j in range(0,90):
               b,g,r = moustache[i][j][:]
               if b<170 or g<170 or r<170:
                 try:
                   img[y+i][j+(x-45)][:] = r,g,b 
                 except:
                   print("out of bounds")
    return img
