import cv2
import matplotlib.pyplot as plt
import numpy as np
from CLASSES import *

# Path to the model you want to use
model_path = "models/fer_emotion_model.hdf5"

# Initialize instance of the model to evaluate the inputs
emotion_classifier = DetectionModel(model_path)

# Initialize video stream instance
webcam = VideoStream()


def main():

    webcam.start()

    while True:

        frame = webcam.frame
        frame = cv2.rotate(frame, cv2.ROTATE_180) # COMMENT THIS LINE IF YOUR IMAGE IS UPSIDE DOWN

        # Detect the faces
        emotion_classifier.predict(frame)
        try:
            emotion_classifier.top_emotion()
        except Exception as e:
            print(e)

        try:
            ce, de, es = emotion_classifier.unpack()
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
        cv2.putText(frame, str(webcam.fps), (7, 70), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 0), 2)

        # Show frame
        cv2.imshow('Filter', frame)

        # Stop if escape key is pressed
        if cv2.waitKey(1) == 27:
            break

    # Release the VideoCapture object
    webcam.destroy()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        webcam.thread.join()
        emotion_classifier.thread.join()
