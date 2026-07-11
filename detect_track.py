from ultralytics import YOLO
import cv2

# Load pretrained YOLOv8 nano model (fast, lightweight)
model = YOLO('yolov8n.pt')

# Open webcam (0 = default camera)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Webcam not opening")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run detection + tracking together (persist=True keeps track IDs across frames)
    results = model.track(frame, persist=True)

    # Draw boxes, labels, and track IDs on frame
    annotated_frame = results[0].plot()

    cv2.imshow('YOLOv8 Detection + Tracking', annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()