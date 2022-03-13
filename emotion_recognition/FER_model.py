from fer import FER
import cv2

def get_emotion(file_path):
    file = cv2.imread(file_path)
    emotion_detector = FER(mtcnn=True)
    captured_emotions = emotion_detector.detect_emotions(file)
    dominant_emotion, emotion_score = emotion_detector.top_emotion(file)
    return captured_emotions, dominant_emotion, emotion_score


for image in ['test.jpeg', 'test_2.jpg', 'test_3.jpg', 'test_4.png', 'test_5.png']:
    result = get_emotion('test_images/' + image)
    print(result[1], result[2])
