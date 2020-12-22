import cv2
class VideoCam(object):
    def __init__(self):
        print("initialized")
        self.vedio = cv2.VideoCapture(0)
        print(self.vedio.read())

    def __del__(self):
        self.vedio.release()

    def get_frame(self):
        ret, frame = self.vedio.read()
        print(frame)
        # DO WHAT YOU WANT WITH TENSORFLOW / KERAS AND OPENCV
        #ret, jpeg = cv2.imencode('.jpg', frame)
        return frame
