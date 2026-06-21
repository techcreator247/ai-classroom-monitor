import streamlit as st
import cv2
import time
from datetime import datetime
import pandas as pd
import plotly.graph_objects as go

from student_detector import detect_students
from attention import check_attention
from utils import calculate_score


# ================= PAGE CONFIG =================
st.set_page_config(page_title="AI Classroom Monitor PRO", layout="wide")
st.title("🎓 AI Classroom Monitoring System")


# ================= SESSION STATE =================
if "run" not in st.session_state:
    st.session_state.run = False

if "cap" not in st.session_state:
    st.session_state.cap = None

if "report" not in st.session_state:
    st.session_state.report = []


# ================= SIDEBAR =================
menu = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "Live Monitor", "Attendance", "Analytics", "Reports"]
)


# ================= UTILITY =================
def generate_student_ids(count):
    return [f"Student_{i+1}" for i in range(count)]


# ================= DASHBOARD =================
if menu == "Dashboard":

    st.header("📊 Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("👥 Students", "Live")
    col2.metric("🎯 Focus", "Live")
    col3.metric("🥱 Drowsy", "Live")
    col4.metric("😴 Sleeping", "Live")

    st.info("Go to Live Monitor to start AI system.")


# ================= LIVE MONITOR =================
elif menu == "Live Monitor":

    st.header("🎥 Live Monitoring System")

    # -------- BUTTONS --------
    colA, colB = st.columns(2)

    with colA:
        if st.button("▶ Start Camera"):
            st.session_state.run = True
            st.session_state.cap = cv2.VideoCapture(0)
            st.session_state.cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

    with colB:
        if st.button("⛔ Stop Camera"):
            st.session_state.run = False
            if st.session_state.cap:
                st.session_state.cap.release()
                st.session_state.cap = None


    # -------- UI PLACEHOLDERS --------
    frame_box = st.empty()
    gauge_box = st.empty()
    alert_box = st.empty()

    col1, col2, col3, col4, col5, col6 = st.columns(6)

    student_box = col1.empty()
    focus_box = col2.empty()
    distract_box = col3.empty()
    drowsy_box = col4.empty()
    sleep_box = col5.empty()
    talking_box = col6.empty()


    # ================= LIVE LOOP =================
    if st.session_state.run and st.session_state.cap is not None:

        cap = st.session_state.cap

        while st.session_state.run:

            ret, frame = cap.read()

            if not ret:
                alert_box.error("Camera disconnected ❌")
                break

            # ================= AI PROCESSING =================
            frame, students = detect_students(frame)
            frame, levels = check_attention(frame)

            score = calculate_score(levels)

            # ================= OVERLAY =================
            cv2.putText(frame, f"Score: {score}", (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 255, 0), 2)

            cv2.putText(frame, f"Students: {students}", (20, 80),
                        cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (255, 0, 0), 2)

            # ================= GAUGE =================
            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=score,
                title={"text": "Attention Score"},
                gauge={"axis": {"range": [0, 100]}}
            ))

            gauge_box.plotly_chart(fig, use_container_width=True, key=f"g_{time.time()}")

            # ================= METRICS =================
            student_box.metric("👥 Students", students)
            focus_box.metric("🎯 Focused", levels.get("Focused", 0))
            distract_box.metric("🟠 Distracted", levels.get("Distracted", 0))
            drowsy_box.metric("🥱 Drowsy", levels.get("Drowsy", 0))
            sleep_box.metric("😴 Sleeping", levels.get("Sleeping", 0))
            talking_box.metric("😂 Talking", levels.get("Talking", 0))

            # ================= FRAME =================
            frame_box.image(frame, channels="BGR", use_container_width=True)

            # ================= ALERTS =================
            if levels.get("Sleeping", 0) > 1:
                alert_box.error("😴 Sleeping detected")
            elif levels.get("Drowsy", 0) > 2:
                alert_box.warning("🥱 Drowsiness detected")
            elif levels.get("Talking", 0) > 3:
                alert_box.warning("😂 Talking detected")

            # ================= ATTENDANCE (STUDENT ID BASED) =================
            student_ids = generate_student_ids(students)

            for sid in student_ids:
                st.session_state.report.append({
                    "student_id": sid,
                    "status": "Present" if score > 50 else "Absent",
                    "score": score,
                    "focused": levels.get("Focused", 0),
                    "drowsy": levels.get("Drowsy", 0),
                    "sleeping": levels.get("Sleeping", 0),
                    "talking": levels.get("Talking", 0),
                    "time": datetime.now()
                })

            time.sleep(0.03)


# ================= ATTENDANCE =================
elif menu == "Attendance":

    st.header("🧾 Attendance Sheet (Student ID Based)")

    if len(st.session_state.report) == 0:
        st.warning("No data yet. Start Live Monitor.")

    else:
        df = pd.DataFrame(st.session_state.report)

        attendance_df = df[["student_id", "status", "score"]]

        st.dataframe(attendance_df)

        st.success(f"Total Student Records: {df['student_id'].nunique()}")


# ================= ANALYTICS =================
elif menu == "Analytics":

    st.header("📈 Analytics")

    if len(st.session_state.report) == 0:
        st.warning("No data available.")

    else:
        df = pd.DataFrame(st.session_state.report)

        st.line_chart(df["score"])

        st.dataframe(df)


# ================= REPORTS =================
elif menu == "Reports":

    st.header("📄 Reports")

    if len(st.session_state.report) == 0:
        st.warning("No reports yet.")

    else:
        df = pd.DataFrame(st.session_state.report)

        st.dataframe(df)

        st.download_button(
            "⬇ Download Report",
            df.to_csv(index=False),
            "attendance_report.csv",
            "text/csv"
        )