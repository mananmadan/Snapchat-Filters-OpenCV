## SnapChat Filters Using OpenCV
An attempt to create and understand the working of snapchat filters using facial landmark tracking
- Also checkout my work on facial landmark tracking [Facial-Keypoints](https://github.com/mananmadan/Facial-Keypoints)


## Main Idea
- Image --> CNN --> Output Co-ordinates of the landmarks
- Then use these co-ordinates to place filters on the image 

## Dataset for Face Detection
- [Data](https://www.kaggle.com/drgilermo/face-images-with-marked-landmark-points)

## To Run
- Since the data set only contain image of size 96,96,1
- Hence haar-cascade is used to first isolate the face and that is passed into model
- The model detects the landmarks and passes it to ``filter.py`` which will then apply the filter to the image
- Then image processing is done to re-adjust the image in the vedio
- ``vedio.py`` runs the network on vedio


## Output

Vedio Output
============
- ![output](output/output.gif)


## Technologies
![opencv](opencv.png) ![tf-keras](tf-keras.jpeg)

## TODO
- Add filters for mouth also! (using the lip tracking mechanism!)
- Make a youtube vedio for it!
- Make a flask web app
