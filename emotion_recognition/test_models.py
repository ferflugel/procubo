# from tensorflow.keras.models import load_model
from dynamic_model_classifier import DETECTOR
import cv2
import matplotlib.pyplot as plt
import numpy as np
from time import time
# from tensorflow.keras.preprocessing import image

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

def show_live_video():
    # To capture video from a webcam
    cap = cv2.VideoCapture(0)

    if not (cap.isOpened()):
        print('Could not open video device')

    prevFrame = 0
    newFrame = 0
    fps = 0

    while True:
        # Read the frame
        _, frame = cap.read()
        newFrame = time()
        fps = int(1/(newFrame - prevFrame))
        fps = str(fps)
        prevFrame = newFrame
        # Convert to grayscale
        # gray = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        # Detect the faces
        # frame = cv2.rotate(frame, cv2.ROTATE_180)
        ce, de, es = get_emotion(frame)

        try:
            faces = list(ce[0]['box'])

            # Draw the rectangle around each face
            for x, y, w, h in [faces]:
                fc = frame[y:y + w, x:x + w]
                # crop over resize
                fin = cv2.resize(fc, (224, 224))
                roi = cv2.resize(fc, (224, 224))
                roi = np.expand_dims(roi, axis=0)
                rounded_prediction = es
                emotion = de
                print(de)
                cv2.putText(frame, str(emotion), (x, y), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 0), 2)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            if cv2.waitKey(1) == 27:
                break
        except:
            pass
        try:
            print(f"{de}: {es*100}%\n")
        except TypeError:
            print("Not recognized...")
        cv2.putText(frame, fps, (7, 70), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 0), 2)
        cv2.imshow('Filter', frame)

        # Stop if escape key is pressed
        # k = cv2.waitKey(30) & 0xff
        # if k == 27:
        #     break
    # Release the VideoCapture object
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    show_live_video()
