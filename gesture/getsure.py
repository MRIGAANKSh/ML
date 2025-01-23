import cv2
import mediapipe as mp
import pyautogui

x1=y1=x2=y2=0
webcam = cv2.VideoCapture(0)
mhands = mp.solutions.hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
drawing_utils = mp.solutions.drawing_utils

while True:
    ret, imag = webcam.read()
    imag=cv2.flip(imag,1)
    if not ret:
        break
    frame_height, frame_width, _ = imag.shape

    
    rgb_img = cv2.cvtColor(imag, cv2.COLOR_BGR2RGB)
    output = mhands.process(rgb_img)
    hands = output.multi_hand_landmarks

    if hands:
        for hand in hands:
            # Draw landmarks on the hand
            drawing_utils.draw_landmarks(imag, hand, mp.solutions.hands.HAND_CONNECTIONS)
            
            # Process each landmark
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width) 
                y = int(landmark.y * frame_height)  

                
                if id == 8:  
                    cv2.circle(img=imag, center=(x, y), radius=8, color=(0, 255, 255), thickness=5)
                    x1=x
                    y1=y
                if id == 4:  
                    cv2.circle(img=imag, center=(x, y), radius=8, color=(0, 0, 255), thickness=5)
                    x2=x
                    y2=y
        dist=((x2-x1)**2+(y2-y1)**2)**(0.5)//4
        cv2.line(imag,(x1,y1),(x2,y2),color=(0,255,0))
        if dist>50:
            pyautogui.press("volumeup")
        else:
            pyautogui.press("volumedown")



    
    cv2.imshow("Hand Volume Gesture", imag)

    
    key = cv2.waitKey(10)
    if key == 27:
        break


webcam.release()
cv2.destroyAllWindows()
