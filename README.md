## SnapChat Filters Using OpenCV
An attempt to create and understand the working of snapchat filters using facial landmark tracking
- Also chekout my work on facial landmark tracking [Facial-Keypoints](https://github.com/mananmadan/Facial-Keypoints)


## Main Idea
- Image --> CNN --> Output Co-ordinates of the landmarks
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
- See how can you instruct the type of filter during python file runtime!
    -```python vedio.py --filter -a -b -c ``` etc. type!
- Test with adding filter using image (Gogles!) instead of creating own filters
- Make the code more modular!
- Add Images of different types of Glasses (Like lenskart!)
- Add filters for mouth also! (using the lip tracking mechanism!)
- Make a youtube vedio for it!
- Make a flask web app