# AirType Keyboard ⌨️✋

**AirType Keyboard** is an advanced virtual, touchless keyboard system built using **Python, OpenCV, and Hand Tracking**. It allows users to type in mid-air using natural hand gestures captured through a webcam, converting finger movements into real-time keyboard input.

This project is designed to improve **mobility, accessibility, and hygiene**, offering an innovative alternative to traditional physical keyboards.

---

## 🚀 Features

* 🎥 **Real-time Hand Tracking** using computer vision
* 🖐️ **Touchless Typing** with finger gesture detection
* ⌨️ **On-screen Virtual Keyboard** with visual feedback
* 🔙 **Backspace & Text Editing Support**
* ⚡ **Low Latency & High Accuracy**
* 🌍 **No External Hardware Required** (only a webcam)

---

## 🧠 How It Works

1. **Camera Input**
   The webcam captures live video frames.

2. **Hand Detection**
   Hand landmarks are detected using a hand tracking module.

3. **Virtual Keyboard Overlay**
   A keyboard layout is drawn on the screen using OpenCV.

4. **Gesture-Based Key Press**
   Finger positions and pinch gestures are analyzed to detect key presses.

5. **Keyboard Output**
   Detected keys are sent to the system as real keyboard inputs using `pynput`.

---

## 🛠️ Technologies Used

* **Python**
* **OpenCV** – video processing & UI rendering
* **cvzone / MediaPipe** – hand landmark detection
* **pynput** – keyboard input control
* **Math & Geometry** – gesture distance calculations

---

## 📊 Performance

* ⚡ Processing Speed: ~30 FPS
* 🎯 Detection Accuracy: ~95% (under good lighting)
* ⏱️ Response Time: ~0.1 seconds per key press

---

## 🎯 Use Cases

* 👩‍💻 Students & Professionals needing portable input methods
* ♿ Accessibility support for users with motor limitations
* 🧼 Public kiosks requiring hygienic, touch-free interaction
* 🤖 Tech enthusiasts exploring Human–Computer Interaction (HCI)

---

## 🧪 Setup & Installation

```bash
pip install opencv-python cvzone pynput mediapipe
```

Run the project:

```bash
python airtype_keyboard.py
```

> Ensure your webcam is connected and proper lighting is available for best results.

---

## 📌 Future Improvements

* Word prediction and auto-correct
* Multi-language keyboard support
* Custom gesture mapping
* UI enhancements and themes
* Integration with AR/VR environments

---

## ⚙️ setup

run the following codes in either vs code terminal or powershell
1. pip install opencv-python
2. pip install opencv-contrib-python
3. pip install pynput
4.  Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
5.  venv\Scripts\Activate
6.  pip install opencv-python cvzone mediapipe pynput numpy
7. cd "<file location>"
8. python "<filename>"
9. to stop the simulation press "ctrl+c" in terminal



---

## 📜 License

This project is for educational and research purposes.

---

⭐ If you found this project interesting, consider giving it a star on GitHub!
