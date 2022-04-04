from CLASSES import *
from openrgb import OpenRGBClient
from openrgb.utils import RGBColor

try:
    client = OpenRGBClient()  # Initialize OpenRGB client
    client.clear()  # Clear all LEDs
    print("CONNECTED")
except:
    print("SOMETHING WENT WRONG WHEN CONNECTING TO THE OpenRGB SERVER...\n\tKILLING PROCESS...")

model_path = "models/fer_emotion_model.hdf5"  # Path to the model you want to use
emotion_classifier = DetectionModel(model_path)  # Initialize the model
webcam = VideoStream()  # Initialize video stream instance
emotion_to_color = {'neutral': (122, 122, 122),
                    'happy': (0, 255, 0),
                    'sad': (0, 0, 255),
                    'fear': (88, 88, 88),
                    'surprise': (168, 50, 156),
                    'disgust': (119, 168, 50),
                    'angry': (255, 0, 0)}  # Dictionary of colors for each emotion

def led_control(emotion, confidence, streak):
    if confidence > 0.8 or streak > 5:
        colors = emotion_to_color[emotion]  # If the emotion is recognized, get the color
        client.set_color(RGBColor(colors[0], colors[1], colors[2]))  # Set the color of the LED
        print(f"{emotion}: {confidence * 100}%\n")

def main():

    webcam.start()  # Start the video stream
    previous_emotion = None
    streak = 0  # Initialize streak of consecutive emotions

    while True:
        frame = webcam.frame  # Get the frame from the video stream
        frame = cv2.rotate(frame, cv2.ROTATE_180) # Rotate the frame 180 degrees

        emotion_classifier.predict(frame)  # Predict the emotion
        try:
            emotion_classifier.top_emotion()  # Get the top emotion
        except Exception as e:
            print(e)

        try:
            ce, emotion, confidence = emotion_classifier.unpack()
            faces = list(ce[0]['box'])

            for x, y, w, h in [faces]:
                if emotion == previous_emotion:
                    streak += 1
                else:
                    streak = 0
                    previous_emotion = emotion

                led_control(emotion, confidence, streak)  # Control the LED's color

                cv2.putText(frame, str(emotion), (x, y), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 0), 2)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Draw a rectangle around the face

        except:
            print("Not recognized...")

        cv2.putText(frame, str(webcam.fps), (7, 70), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 0), 2)  # Display the FPS
        cv2.imshow('Filter', frame)  # Show the frame
        if cv2.waitKey(1) == 27:  # If the user presses ESC, break the loop
            break

    webcam.destroy()  # Release the video stream


if __name__ == "__main__":
    try:
        client.clear()
        main()
    except KeyboardInterrupt:
        webcam.thread.join()
        emotion_classifier.thread.join()
