import cv2

name = input("Enter your name: ")
cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    cv2.imshow("Register Retina", frame)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite(f"retina_dataset/{name}.jpg", frame)
        print(f"[INFO] Retina saved as {name}.jpg")
        break

cam.release()
cv2.destroyAllWindows()
