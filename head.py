import cv2
import numpy as np
import mediapipe as mp

mp_face = mp.solutions.face_mesh.FaceMesh()

def estimate_head_pose(frame):
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    res = mp_face.process(rgb)

    if not res.multi_face_landmarks:
        return "Unknown"

    face = res.multi_face_landmarks[0]

    nose = face.landmark[1]

    if nose.x < 0.4:
        return "Left"
    elif nose.x > 0.6:
        return "Right"
    else:
        return "Center"