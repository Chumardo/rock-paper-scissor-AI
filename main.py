import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import time
import random

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

ROCK = [0, 0, 0, 0, 0]
PAPER = [1, 1, 1, 1, 1]
SCISSOR = [0, 1, 1, 0, 0]

detector = HandDetector(maxHands=1)

timer = 0
state_result = False
start_game = False

while True:
    img_bg = cv2.imread("Resources/BG.png")
    success, img = cap.read()

    img_scaled = cv2.resize(img,(0,0),None,0.875,0.875)
    img_scaled = img_scaled[:,80:480]
    
    hands, img = detector.findHands(img_scaled)
    
    if start_game:
        
        if state_result is False:
            timer = time.time() - initial_time
            cv2.putText(img_bg, str(int(timer)), (604, 435), cv2.FONT_HERSHEY_PLAIN,6,(255,0,255),16)

            if timer > 3:
                state_result = True
                timer = 0

                if hands:
                    hand = hands[0]
                    fingers = detector.fingersUp(hand)
                    if fingers == ROCK:
                        player_move = 1
                    if fingers == PAPER:
                        player_move = 2
                    if fingers == SCISSOR:
                        player_move = 3
                    
                    
                    ai_choice = random.choice(['rock', 'paper', 'scissor'])
                    img_ai = cv2.imread(f'Resources/{ai_choice}.png', cv2.IMREAD_UNCHANGED)    
                    img_bg = cvzone.overlayPNG(img_bg,img_ai,(149,310))
                    
                    print(player_move)
    
    img_bg[234:654,795:1195] = img_scaled

    if state_result:
        img_bg = cvzone.overlayPNG(img_bg,img_ai,(149,310))
    
    
    cv2.imshow("BG", img_bg)
    
    key = cv2.waitKey(1)
    if key == ord('s'):
        start_game = True
        initial_time = time.time()
        state_result = False