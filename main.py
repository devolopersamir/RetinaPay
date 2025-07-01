import cv2
import face_recognition
import os
import numpy as np
import requests

known_encodings = []
known_names = []

# Load saved retina images
for filename in os.listdir("retina_dataset"):
    if filename.endswith(".jpg"):
        image = face_recognition.load_image_file(f"retina_dataset/{filename}")
        encoding = face_recognition.face_encodings(image)[0]
        known_encodings.append(encoding)
        known_names.append(filename.split(".")[0])

cap = cv2.VideoCapture(0)

print("[INFO] Scanning retina...")

while True:
    success, frame = cap.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    faces = face_recognition.face_locations(rgb)
    encodings = face_recognition.face_encodings(rgb, faces)

    for encoding in encodings:
        matches = face_recognition.compare_faces(known_encodings, encoding)
        name = "Unknown"

        if True in matches:
            index = matches.index(True)
            name = known_names[index]
            print(f"[SUCCESS] Retina matched with user: {name}")

            amount = input("Enter amount to withdraw: ")
            response = requests.post("http://127.0.0.1:5000/withdraw", json={
                "user": name,
                "amount": int(amount)
            })
            print(response.json())
            break

    cv2.imshow("Retina Scanner ATM", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
