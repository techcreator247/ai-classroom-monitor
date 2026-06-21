import cv2
import mediapipe as mp
import math

from drowsiness import detect_drowsiness
from head import estimate_head_pose
from talk import detect_talking

mp_face = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)

def dist(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)


def check_attention(frame):

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = mp_face.process(rgb)

    levels = {
        "Focused": 0,
        "Distracted": 0,
        "Drowsy": 0,
        "Sleeping": 0,
        "Talking": 0
    }

    if result.multi_face_landmarks:

        for face in result.multi_face_landmarks:

            left_eye_top = face.landmark[159]
            left_eye_bottom = face.landmark[145]
            nose = face.landmark[1]

            eye_open = dist(left_eye_top, left_eye_bottom)

            drowsy = detect_drowsiness(frame)
            head = estimate_head_pose(frame)
            talking = detect_talking(frame)

            if drowsy:
                levels["Drowsy"] += 1

            if head in ["Left", "Right"]:
                levels["Distracted"] += 1
            else:
                levels["Focused"] += 1

            if talking:
                levels["Talking"] += 1

            if eye_open < 0.015:
                levels["Sleeping"] += 1

    return frame, levels