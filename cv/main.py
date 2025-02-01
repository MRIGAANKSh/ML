from ultralytics import YOLO  # Corrected import
import cv2
import cvzone
# Load the model
model = YOLO("yolov8n.pt")  # Corrected function call
print("Model loaded")
result=model("1.webp",show=True)
cv2.waitKey(0)