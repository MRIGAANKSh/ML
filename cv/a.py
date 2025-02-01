from ultralytics import YOLO
import cv2
import cvzone


cap = cv2.VideoCapture(0)  # For Webcam
cap.set(3, 1280)
cap.set(4, 720)
model = YOLO("yolov8n.pt")

