import mediapipe as mp

print("FILE:", mp.__file__)
print("HAS SOLUTIONS:", hasattr(mp, "solutions"))
print("DIR CHECK:", "solutions" in dir(mp))