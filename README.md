# Drowsiness_Detection
The Drowsiness Detection program is a python based program used to detect drowsiness in drivers during driving.

# Drowsiness Detection System

## 📌 Overview

The **Drowsiness Detection System** is a real-time application that monitors a driver's eye activity using **computer vision** and **machine learning techniques**. The system alerts the driver with an alarm sound when signs of drowsiness are detected.

## 🚀 Features

- **Real-Time Face Detection:** Uses Dlib’s pre-trained **HOG** and **CNN** models for face recognition.
- **Facial Landmark Detection:** Identifies **68 facial landmarks** to track eye movement.
- **Eye Aspect Ratio (EAR) Calculation:** Detects eye closure by analyzing the EAR threshold.
- **Drowsiness Detection Logic:** If the EAR remains below a threshold for a consecutive number of frames, an alert is triggered.
- **Alert System:** Uses **pyglet** to play an alarm sound if drowsiness is detected.

## 🛠️ Tech Stack

- **Python**
- **OpenCV** (Computer Vision)
- **Dlib** (Face and landmark detection)
- **NumPy** (Numerical computations)
- **Scipy** (Euclidean distance calculations)
- **Imutils** (Simplified OpenCV operations)
- **Pyglet** (Sound playback for alarms)

## 📂 Project Structure

```
Drowsiness-Detection-System/
│── drowsy.py               # Main script for detection
│── mixkit-classic-alarm-995.wav  # Alarm sound file
│── 68_face_landmarks.dat   # Pre-trained facial landmark model
│── README.md               # Project documentation
```

## 🔧 Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/drowsiness-detection.git
   cd drowsiness-detection
   ```
2. Install dependencies:
   ```sh
   pip install opencv-python opencv-contrib-python dlib numpy scipy imutils pyglet
   ```
3. Ensure **`68_face_landmarks.dat`** is in the project directory.
4. Run the program:
   ```sh
   python drowsy.py
   ```

## 🖥️ How It Works

1. The **webcam** captures live video of the driver.
2. **Dlib’s face detector** locates the face in the frame.
3. **Facial landmarks** identify key eye points.
4. The **Eye Aspect Ratio (EAR)** is calculated.
5. If the EAR drops below **0.25** for **20 consecutive frames**, an alarm is triggered.
6. The driver is **alerted via sound** to prevent accidents.

## 🎯 Future Enhancements

- **Head Pose Estimation** for more accurate detection.
- **Integration with Vehicle Systems** to slow down the car when drowsiness is detected.
- **Cloud-Based Data Logging** to store driver drowsiness history.

## ⚠️ Known Issues

- **Webcam Not Opening:** Ensure **OpenCV** is installed with GUI support (`opencv-python-headless` may cause issues).
- **Shape Predictor Model Not Found:** Download `68_face_landmarks.dat` and place it in the project directory.
- **Dlib Whl Issue** Make sure that the Dlib files are downloaded properly for the project. 

## 🤝 Contributing

Feel free to submit **pull requests** or open an **issue** to improve the project!

## Thanks for viewing my Project!


PS - Here is a drive **link** for downloading the dat file **(68_facial_landmarks.dat)**
link - https://drive.google.com/file/d/1WQyNLow3QK-PYIzDIyCZ-mCWgDwFMG5O/view?usp=sharing

**This link contains a single file of 97,358kb. This is a virus free dat.file**


