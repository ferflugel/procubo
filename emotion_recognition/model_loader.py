from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import cv2
import numpy as np

def emotion_analysis(emotion):
    objects = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']
    return objects[emotion]

def process_image(file_path):
    file = open(file_path, 'rb')
    file_string = file.read()
    np_img = np.frombuffer(file_string, np.uint8)
    img = cv2.imdecode(np_img, cv2.IMREAD_UNCHANGED)
    if len(img.shape) == 3:
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    x = cv2.resize(img, (48, 48))
    x = image.img_to_array(x)
    x = np.expand_dims(x, axis=0)
    return x

def get_emotion(file_path, model):
    test_image = process_image(file_path)
    custom = model.predict(test_image)
    output = custom.argmax(axis=1)
    output = emotion_analysis(output[0])
    return output


# Testing the model
emotion_model = load_model('baseline.h5')
emotion_output = get_emotion('test_images/test_2.jpg', emotion_model)
# emotion_output = get_emotion('images/validation/disgust/1115.jpg', emotion_model)
