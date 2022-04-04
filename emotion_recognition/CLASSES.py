from dynamic_model_classifier import DETECTOR
import cv2, queue
from threading import Thread
import numpy as np
from time import time

class VideoStream:
    def __init__(self, src=0):
        self.stream = cv2.VideoCapture(src)
        if not (self.stream.isOpened()):
            print('Could not open video device')

        (self.grabbed, self.frame) = self.stream.read()
        self.fps = 0
        self.thread = None
        self.stopped = False

    def start(self):
        self.thread = Thread(target=self.update, args=()).start()
        return self

    def update(self):
		# keep looping infinitely until the thread is stopped
        prevFrame = 0
        newFrame = 0
        while True:
			# if the thread indicator variable is set, stop the thread
            if self.stopped:
                break
			# otherwise, read the next frame from the stream
            (self.grabbed, self.frame) = self.stream.read()

            # Calculate FPS
            newFrame = time()
            self.fps = int(1/(newFrame - prevFrame))
            prevFrame = newFrame

    def rotateFrame(self):
        self.frame = cv2.rotate(self.frame, cv2.ROTATE_180)

    def read(self):
        # return the frame most recently read
        return self.frame

    def stop(self):
        # indicate that the thread should be stopped
        self.stopped = True

    def destroy(self):
        self.stream.release()
        cv2.destroyAllWindows()

class DetectionModel:
    def __init__(self, modelPath, faceDetector="haar"):
        if faceDetector == "haar":
            self.classifier = DETECTOR(modelPath)
        elif faceDetector == "ssd":
            self.classifier = DETECTOR(modelPath, ssd=True)
        elif faceDetector == "mtcnn":
            elf.classifier = DETECTOR(modelPath, mtcnn=True)

        self.predictions = None
        self.dominant_emotion = None
        self.emotion_score = None
        self.thread = None

    def top_emotion(self):

        top_emotions = [
            max(e["emotions"], key=lambda key: e["emotions"][key]) for e in self.predictions
        ]

        # Take first face
        if len(top_emotions):
            top_emotion = top_emotions[0]
        else:
            return (None, None)
        score = self.predictions[0]["emotions"][top_emotion]

        self.dominant_emotion = top_emotion
        self.emotion_score = score

    def predict(self, img: np.ndarray):
        try:
            img = cv2.imread(img, 1)  # File passed as path
        except TypeError:
            img = img  # If file was passed as np.ndarray


        # IMPORTANT - Need to get return from function inside the Thread()
        # self.thread = Thread(target=self.classifier.detect_emotions(img), args=(img, )).start()
        self.predictions = self.classifier.detect_emotions(img)

    def unpack(self):
        return self.predictions, self.dominant_emotion, self.emotion_score
