import cv2

# Load Haar cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

if face_cascade.empty():
    print(" Haar cascade failed to load.")
    exit()

# Open the camera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print(" Could not open webcam.")
    exit()

print(" Webcam is active. Press ESC to exit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print(" Failed to capture frame.")
        break

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    print(f" Detected {len(faces)} face(s)")

    # Draw rectangles
    for (x, y, w, h) in faces:
        print(f" Drawing rectangle at x:{x}, y:{y}, w:{w}, h:{h}")
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Create a named window to ensure display
    cv2.namedWindow("Face Detection", cv2.WINDOW_NORMAL)
    cv2.imshow("Face Detection", frame)

    # Exit if ESC is pressed
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
