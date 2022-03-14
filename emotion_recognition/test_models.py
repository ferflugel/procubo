from tensorflow.keras.models import load_model
from dynamic_model_classifier import DETECTOR
import cv2, os

#Path to the model you want to use
model_path = "models/baseline4.h5"

#Initialize instance of the model to evaluate the inputs
emotion_classifier = DETECTOR(model_path)

def get_emotion(file_path):
    file = cv2.imread(file_path, 1)
    captured_emotions = emotion_classifier.detect_emotions(file)
    dominant_emotion, emotion_score = emotion_classifier.top_emotion(file)
    return captured_emotions, dominant_emotion, emotion_score

for image in os.listdir('test_images'):
    result = get_emotion('test_images/' + image)
    print(image, "\t:", result[1], result[2])
