import cv2
import numpy as np
import mediapipe as mp

mp_face = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)

def eye_aspect_ratio(eye):
    A = np.linalg.norm(np.array([eye[1].x, eye[1].y]) - np.array([eye[5].x, eye[5].y]))
    B = np.linalg.norm(np.array([eye[2].x, eye[2].y]) - np.array([eye[4].x, eye[4].y]))
    C = np.linalg.norm(np.array([eye[0].x, eye[0].y]) - np.array([eye[3].x, eye[3].y]))
    return (A + B) / (2.0 * C)

def detect_drowsiness(frame):
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    res = mp_face.process(rgb)

    drowsy = False

    if res.multi_face_landmarks:
        for face in res.multi_face_landmarks:
            left_eye = [face.landmark[i] for i in [33, 160, 158, 133, 153, 144]]
            right_eye = [face.landmark[i] for i in [362, 385, 387, 263, 373, 380]]

            ear = (eye_aspect_ratio(left_eye) + eye_aspect_ratio(right_eye)) / 2

            if ear < 0.18:
                drowsy = True

    return drowsy