from dynamic_model_classifier import DETECTOR
import cv2
import matplotlib.pyplot as plt
import numpy as np
from time import time


# Path to the model you want to use
model_path = "models/fer_emotion_model.hdf5"

# Initialize instance of the model to evaluate the inputs
emotion_classifier = DETECTOR(model_path)

def get_emotion(file):
    try:
        file = cv2.imread(file, 1)  # File passed as path
    except TypeError:
        file = file  # If file was passed as np.ndarray

    captured_emotions = emotion_classifier.detect_emotions(file)
    dominant_emotion, emotion_score = emotion_classifier.top_emotion(file)
    return captured_emotions, dominant_emotion, emotion_score

def get_frame(device):
    rt, fr = device.read()
    return rt, fr

def show_live_video():
    # To capture video from a webcam
    cap = cv2.VideoCapture(-1)

    if not (cap.isOpened()):
        print('Could not open video device')

    prevFrame = 0
    newFrame = 0
    fps = 0

    while True:
        # Read the frame
        _, frame = get_frame(cap)

        # Calculate FPS
        newFrame = time()
        fps = int(1/(newFrame - prevFrame))
        fps = str(fps)
        prevFrame = newFrame

        # Rotate frame 180 degrees
        frame = cv2.rotate(frame, cv2.ROTATE_180)  # COMMENT THIS LINE IF YOUR IMAGE IS UPSIDE DOWN

        # Detect the faces
        ce, de, es = get_emotion(frame)

        try:
            faces = list(ce[0]['box'])

            # Draw the rectangle around each face
            for x, y, w, h in [faces]:
                rounded_prediction = es
                emotion = de
                cv2.putText(frame, str(emotion), (x, y), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 0), 2)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            print(f"{de}: {es*100}%\n")
        except:
            print("Not recognized...")

        # Put FPS on frame
        cv2.putText(frame, fps, (7, 70), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 0), 2)

        # Show frame
        cv2.imshow('Filter', frame)

        # Stop if escape key is pressed
        if cv2.waitKey(1) == 27:
            break

    # Release the VideoCapture object
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    show_live_video()
    # Release the VideoCapture object
    try:
        cap.release()
    except:
        pass
    cv2.destroyAllWindows()
