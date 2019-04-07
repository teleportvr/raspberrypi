import cv2

class VideoCamera(object):

    def __init__(self):
        self.cap = cv2.VideoCapture(2)

    def __del__(self):
        self.cap.release()

    def get_frame(self):
        ret, frame = self.cap.read()
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()
