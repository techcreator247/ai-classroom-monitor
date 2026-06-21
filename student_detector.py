from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

def detect_students(frame):
    results = model(frame, verbose=False)

    count = 0

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])

            if cls == 0:  # person
                count += 1

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    return frame, count