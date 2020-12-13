from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import time
import cv2 
import os
import numpy
## supress tensorflow warning
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
from tensorflow.keras.models import load_model
from filter import filtering,apply

## load model
# model1 is better than model
model = tf.keras.models.load_model('model/model1.h5',compile = False)
#model = tf.keras.models.load_model('model/model.h5',compile = False)

def detect_points(face_img):
    me  = np.array(face_img)
    x_test = np.expand_dims(me, axis=0)
    x_test = np.expand_dims(x_test, axis=3)

    y_test = model.predict(x_test)
    
    return y_test
    
# Load haarcascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
dimensions = (96, 96)
types = "moustache"
## declare vid object
vid = cv2.VideoCapture(0)
while True:
    ## Process the frame
    ret,frame = vid.read()
    img = frame ## 480 640 3
    default_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_img, 1.3, 5)
    faces_img = np.copy(gray_img)
    plt.rcParams["axes.grid"] = False


    ## No face found
    if len(faces) == 0:
        print("No faces found!")

    for i, (x,y,w,h) in enumerate(faces):
        ## isolate the face
        just_face = cv2.resize(gray_img[y:y+h,x:x+w], dimensions)
        just_color_face = cv2.resize(img[y:y+h,x:x+w], dimensions)
        
        ## get landmarks
        label_point = detect_points(just_face)
        
        ##apply all the filters you want
        filtered_points = filtering(label_point,"glasses")
        just_color_face = apply(just_color_face,filtered_points,"glasses")
        filtered_points = filtering(label_point,"moustache")
        just_color_face = apply(just_color_face,filtered_points,"moustache")

        ## resize and fit back the isolated face in original image
        just_color_face = cv2.resize(just_color_face,(h,w))
        img[y:y+h,x:x+w] = just_color_face
        
        # Display the resulting frame 
        cv2.imshow('frame', img) 
      
        # the 'q' button is set as the 
        # quitting button you may use any 
        # desired button of your choice 
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break