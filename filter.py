import cv2

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
  
##get the label points you want for each of the cases
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

## apply filters to the image using crazy maths!
def apply(img,points,types):
    if types == 'glasses':
        global glasses
        x1,y1 = points[0]
        x2,y2 = points[1]
        x1 = int(x1)
        x2 = int(x2)
        y = int((y1+y2)/2)
        y = y-5
        temp = cv2.resize(glasses,((x1-x2)+10,30))
        for i in range(0,temp.shape[0]):
          for j in range(0,temp.shape[1]):
            r,g,b = temp[i,j,:]
            if r<170 or g<170 or b<170:
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
               if b<170 or g<170 or r<170:
                 try:
                   img[y+i][j+(x-45)][:] = r,g,b 
                 except:
                   print("out of bounds")
    return img
