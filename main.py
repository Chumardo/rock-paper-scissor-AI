import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)


detector = HandDetector(maxHands=1)

while True:
    imgBG = cv2.imread("Resources/BG.png")
    success, img = cap.read()

    imgScaled = cv2.resize(img,(0,0),None,0.875,0.875)
    imgScaled = imgScaled[:,80:480]
    
    hands, img = detector.findHands(imgScaled)
    
    if hands:
        hand = hands[0]
        fingers = detector.fingersUp(hand)
    
    imgBG[234:654,795:1195] = imgScaled

    
    
    cv2.imshow("BG", imgBG)
    
    cv2.waitKey(1)
