from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import TensorBoard
import datetime

train_path = 'images/train'
val_path = 'images/validation'
train_data_generator = ImageDataGenerator(rescale=1. / 255)
val_data_generator = ImageDataGenerator(rescale=1. / 255)

train_generator = train_data_generator.flow_from_directory(
        train_path,
        target_size=(48, 48),
        batch_size=64,
        color_mode="grayscale",
        class_mode="categorical")

validation_generator = val_data_generator.flow_from_directory(
        val_path,
        target_size=(48, 48),
        batch_size=64,
        color_mode="grayscale",
        class_mode="categorical")

emotion_model = load_model('baseline4.h5')

log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = TensorBoard(log_dir=log_dir, histogram_freq=1)

emotion_model_info = emotion_model.fit(
        train_generator,
        epochs=40,
        batch_size=200,
        validation_data=validation_generator,
        callbacks=[tensorboard_callback])

emotion_model.save('baseline5.h5')
