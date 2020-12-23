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
- Time everything and see what 
- Use Numpy Operation Instead of Loops for applying filters on the image
- Write an argument parser for command line
- Add filters for mouth also! (using the lip tracking mechanism!)
- Train a face detection algorithm instead of haar-cascades
   - If haar-cascades is taking significant time
- If calculation label points takes time , then save the points for a particular person and only detect if a new person is found
- Make a youtube vedio and blog for it!
- Implement Optical Flow stuff to give a 3D View? 