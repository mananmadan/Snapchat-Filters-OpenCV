## SnapChat Filters Using OpenCV
An attempt to create and understand the working of snapchat filters using facial landmark tracking

- Also chekout my work on facial landmark tracking [Facial-Keypoints](https://github.com/mananmadan/Facial-Keypoints)


## Main Idea
- Image --> CNN --> output co-ordinates of the landmarks
- Then use these co-ordinates to place filters on the image 

## Dataset for face detection
- [Data](https://www.kaggle.com/drgilermo/face-images-with-marked-landmark-points)

## To Run
- Since the data set only contain image of size 96,96,1
- Hence haar-cascade is used to first isolate the face and that is passed into model
- ```vedio.py``` runs the network on vedio from web cam and uptill now only contains the gogles filter.


## Output
Vedio Output
- ![output](output/output.gif)

## TODO
- Add more filters! 
 - HAT
  - first measure the distance of bottom of the hat from the bottom of the image
  - in vedio,scale down the image using the length b/w (outer left/right eyebrow end)
  - then using the scale coeffiecient on the y axis find the value of the bottom point in the image
  - do calculation on the y axis as to where to place the hat image , so that the bottom point in the image , lies at the top of head
  - then do simple masking operation to get the output image