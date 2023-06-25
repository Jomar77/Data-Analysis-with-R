#face detection python
# Date: 5/11/2020
# Name: Hand Detection
# Description: this program detects hands in an image and draws rectangles around them
# Reference: https://www.youtube.com/watch?v=01sAkU_NvOY&list=PLZsOBAyNTZwbK2jTuSZfVfU3CMSK4pVH6&index=2&t=0s
# ======================================================================================================

import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

# mediapipe hands
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0 # previous time
cTime = 0 # current time

while True:
    success, img = cap.read()

    # convert to RGB
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(imgRGB)

    #print(result.multi_hand_landmarks) # prints landmarks on hand

    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                #print(id,lm) # prints id and landmark
                h,w,c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id, cx, cy)
                if id == 0:
                    cv2.circle(img, (cx,cy), 25, (255,0,255), cv2.FILLED)


            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    # calculate fps
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    # display fps
    cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)