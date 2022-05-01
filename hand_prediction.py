from cvzone.HandTrackingModule import HandDetector
import cv2
import cvzone
import serial
# import mediapipe as mp

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=2)

while(True):
    success, img = cap.read()
#     img = detector.findHands(img)
#     print(img)
    hands, img = detector.findHands(img, flipType=False ) # boundingbox(bbox) => hand tracking, with draw
#     hands = detector.findHands(img, draw = False) # no draw
#     print(bbox)
    if hands:
        fingers = detector.fingersUp(hands[0])
#         print(fingers)
#         ser.sendData(fingers)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
#     break