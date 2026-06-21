

# 🎓 AI Classroom Monitoring System (Streamlit + OpenCV)

A real-time AI-powered classroom monitoring system that detects **student attention, drowsiness, distraction, talking behavior, and generates automated attendance reports using computer vision.**

---

## 🚀 Features

* 🎥 Real-time webcam monitoring using OpenCV
* 👥 Student detection using YOLOv8
* 🧠 Attention classification:

  * Focused
  * Distracted
  * Drowsy
  * Sleeping
  * Talking
* 📊 Live attention score gauge (Plotly)
* 🧾 Automatic attendance system (Student ID based)
* 📈 Analytics dashboard (graphs & trends)
* 📄 Report generation & CSV download
* 🖥️ Sidebar navigation (Dashboard, Live, Attendance, Analytics, Reports)

---

## 🏗️ Project Structure

```
AI_Attention_System/
│
├── app.py                  # Main Streamlit application
├── student_detector.py    # YOLO-based person detection
├── attention.py           # Attention classification logic
├── eye.py                 # Eye direction logic (dummy/logic-based)
├── head.py                # Head pose estimation (dummy/logic-based)
├── drowsiness.py         # Drowsiness detection
├── talk.py                # Talking detection
├── utils.py              # Attention score calculation
├── database.py           # Excel report saving
├── style.css             # UI styling
│
├── logs/
│   └── attention_report.xlsx
│
└── README.md
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/ai-classroom-monitor.git
cd ai-classroom-monitor
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
streamlit run app.py
```

---

## 🧠 How It Works

1. Webcam captures live classroom video
2. YOLO detects number of students
3. MediaPipe analyzes facial landmarks
4. System classifies behavior:

   * Focused
   * Distracted
   * Sleeping
   * Talking
5. AI calculates attention score
6. Attendance generated using Student IDs
7. Reports stored for analytics

---

## 🧾 Attendance System

* Student IDs are generated dynamically:

  * Student_1
  * Student_2
  * Student_3
* Status is assigned based on attention score:

  * Score > 50 → Present
  * Score ≤ 50 → Absent

---

## 📊 Modules

### 🎥 Live Monitor

* Real-time video feed
* AI detection overlay
* Attention gauge
* Alerts system

### 🧾 Attendance

* Student-wise attendance sheet
* Present / Absent status
* Exportable data

### 📈 Analytics

* Score trend graph
* Student count trends
* Data visualization

### 📄 Reports

* Full dataset view
* CSV download option

---

## ⚠️ Limitations

* No real face recognition (IDs are generated)
* Simplified attention logic (prototype level)
* Streamlit not optimized for high-FPS video

---

## 🚀 Future Improvements

* 🔐 Face recognition attendance system
* 👨‍🏫 Teacher login panel
* ☁️ Cloud database (Firebase / SQL)
* 😃 Emotion detection upgrade
* 📡 Multi-camera support
* 🌐 WebRTC real-time streaming

---

## 🧑‍💻 Tech Stack

* Python 🐍
* Streamlit ⚡
* OpenCV 🎥
* YOLOv8 🤖
* MediaPipe 🧠
* Plotly 📊
* Pandas 📑

---

## 👨‍🎓 Author

AI Classroom Monitoring System
Built for academic AI + Computer Vision learning

---

## 📜 License

Educational use only.

---


