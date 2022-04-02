# from tensorflow.keras.models import load_model
from dynamic_model_classifier import DETECTOR
import cv2
import numpy as np
from openrgb import OpenRGBClient
from openrgb.utils import RGBColor, DeviceType

emotion_to_color = {'neutral': (122, 122, 122),
                    'happy': (0, 255, 0),
                    'sad': (0, 0, 255),
                    'fear': (88, 88, 88),
                    'surprise': (168, 50, 156),
                    'disgust': (119, 168, 50),
                    'angry': (255, 0, 0)}

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


def led_control(emotion, confidence, streak):
    if confidence > 0.8 or streak > 1:
        colors = emotion_to_color[emotion]
    else:
        colors = emotion_to_color['neutral']

    client.set_color(RGBColor(colors[0], colors[1], colors[2]))


def show_live_video():
    # To capture video from a webcam
    cap = cv2.VideoCapture(2)

    if not (cap.isOpened()):
        print('Could not open video device')

    previous_emotion = None
    streak = 0

    while True:
        # Read the frame
        _, frame = cap.read()
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
                emotion = de
                if emotion == previous_emotion:
                    streak += 1
                else:
                    streak = 0
                    previous_emotion = emotion
                led_control(emotion, es, streak)
                cv2.putText(frame, str(emotion), (x, y), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 0), 2)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            if cv2.waitKey(1) == 27:
                break
        except:
            pass

        cv2.imshow('Filter', frame)

        # Stop if escape key is pressed
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    # Release the VideoCapture object
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    client = OpenRGBClient()
    client.clear()  # Turns everything off
    show_live_video()
