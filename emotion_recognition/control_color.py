from dynamic_model_classifier import DETECTOR
import cv2
from openrgb import OpenRGBClient
from openrgb.utils import RGBColor

emotion_to_color = {'neutral': (122, 122, 122),
                    'happy': (0, 255, 0),
                    'sad': (0, 0, 255),
                    'fear': (88, 88, 88),
                    'surprise': (168, 50, 156),
                    'disgust': (119, 168, 50),
                    'angry': (255, 0, 0)}

model_path = "models/fer_emotion_model.hdf5"  # Path to the trained model
emotion_classifier = DETECTOR(model_path)  # Initialize the classifier

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

    cap = cv2.VideoCapture(2)  # Open the webcam

    if not (cap.isOpened()):
        print('Could not open video device')

    previous_emotion = None
    streak = 0

    while True:
        _, frame = cap.read()  # Read the frame
        ce, emotion, confidence = get_emotion(frame)  # Get the emotion

        try:
            faces = list(ce[0]['box'])  # Get the face coordinates

            # Draw the rectangle around each face
            for x, y, w, h in [faces]:
                if emotion == previous_emotion:
                    streak += 1
                else:
                    streak = 0
                    previous_emotion = emotion
                led_control(emotion, confidence, streak)
                cv2.putText(frame, str(emotion), (x, y), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 0), 2)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            if cv2.waitKey(1) == 27:
                break
        except:
            pass

        cv2.imshow('Filter', frame)

        k = cv2.waitKey(30) & 0xff  # Press 'ESC' for exiting video
        if k == 27:
            break
    cap.release()  # Release the VideoCapture object
    cv2.destroyAllWindows()  # Close all opencv windows


if __name__ == "__main__":
    client = OpenRGBClient()  # Initialize OpenRGB client
    client.clear()  # Clear all LEDs
    show_live_video()  # Show live video
