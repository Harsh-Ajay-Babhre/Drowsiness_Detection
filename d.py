import cv2
import dlib
import numpy as np
from scipy.spatial import distance as dist
from imutils import face_utils
import pyglet
import time
import os

# Initialize sound
alarm = pyglet.media.load('mixkit-classic-alarm-995.wav', streaming=False)

def sound_alarm():
    try:
        alarm.play()
    except Exception as e:
        print(f"Error playing alarm: {e}")

# Compute Eye Aspect Ratio (EAR)
def eye_aspect_ratio(eye):
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])
    C = dist.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

# Thresholds and consecutive frame count
EYE_AR_THRESH = 0.25
EYE_AR_CONSEC_FRAMES = 20

COUNTER = 0

try:
    # Initialize dlib's face detector (correct method)
    detector = dlib.get_frontal_face_detector()
    predictor_path = r"C:\Users\harsh\OneDrive\Desktop\d\68 face landmarks.dat"

    # Check if the shape predictor file exists
    if not os.path.isfile(predictor_path):
        raise FileNotFoundError(f"Shape predictor file not found at {predictor_path}")

    predictor = dlib.shape_predictor(predictor_path)

    # Start video stream
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise OSError("Cannot open webcam")

    # Get eye landmarks
    (lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
    (rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        # Convert frame to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Convert frame to RGB for shape predictor
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Ensure images are 8-bit
        if gray.dtype != np.uint8:
            gray = (gray * 255).astype(np.uint8)
        if rgb_frame.dtype != np.uint8:
            rgb_frame = (rgb_frame * 255).astype(np.uint8)

        # Detect faces in grayscale image
        rects = detector(gray, 0)

        for rect in rects:
            # Pass RGB image to predictor
            shape = predictor(rgb_frame, rect)
            shape = face_utils.shape_to_np(shape)

            leftEye = shape[lStart:lEnd]
            rightEye = shape[rStart:rEnd]
            leftEAR = eye_aspect_ratio(leftEye)
            rightEAR = eye_aspect_ratio(rightEye)

            ear = (leftEAR + rightEAR) / 2.0

            # Visualize eye regions
            leftHull = cv2.convexHull(leftEye)
            rightHull = cv2.convexHull(rightEye)
            cv2.drawContours(frame, [leftHull], -1, (0, 255, 0), 1)
            cv2.drawContours(frame, [rightHull], -1, (0, 255, 0), 1)

            # Check if EAR is below threshold
            if ear < EYE_AR_THRESH:
                COUNTER += 1

                if COUNTER >= EYE_AR_CONSEC_FRAMES:
                    cv2.putText(frame, "DROWSINESS DETECTED!", (10, 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                    sound_alarm()
            else:
                COUNTER = 0

            # Display EAR
            cv2.putText(frame, f"EAR: {ear:.2f}", (300, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

        cv2.imshow("Drowsiness Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

except FileNotFoundError as e:
    print(f"File error: {e}")
except RuntimeError as e:
    print(f"Runtime error: {e}")
except OSError as e:
    print(f"OS error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
