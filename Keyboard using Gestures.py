import cv2
from cvzone.HandTrackingModule import HandDetector
import cvzone
from pynput.keyboard import Key,Controller
import math

# Camera setup
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # width
cap.set(4, 720)   # height
pinched=False

detector = HandDetector(detectionCon=0.8)
keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
        ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/","<--"],]
finalText = ""

keyboard = Controller()


# Draw buttons on screen
def drawAll(img, buttonList):
    for button in buttonList:
        x, y = button.pos
        w, h = button.size
        cvzone.cornerRect(img, (x, y, w, h), 20, rt=0)
        cv2.rectangle(img, button.pos, (x + w, y + h),
                      (255, 0, 255), cv2.FILLED)
        cv2.putText(img, button.text, (x + 20, y + 65),
                    cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
    return img


# Button class
class Button():
    def __init__(self, pos, text, size=[85, 85]):
        self.pos = pos
        self.size = size
        self.text = text


# Create button list
buttonList = []
for i in range(len(keys)):
    for j, key in enumerate(keys[i]):
        buttonList.append(Button([100 * j + 50, 100 * i + 50], key))

# Main loop
while True:
    success, img = cap.read()
    img=cv2.flip(img,1)
    hands, img = detector.findHands(img)
    lmList = []
    bboxInfo = None
    if hands:
        lmList = hands[0]['lmList']       # list of landmarks
        bboxInfo = hands[0]['bbox']       # bounding box [x, y, w, h]

    img = drawAll(img, buttonList)

    if lmList:
        for button in buttonList:
            x, y = button.pos
            w, h = button.size

            # Check if fingertip is inside button
            if x < lmList[8][0] < x + w and y < lmList[8][1] < y + h:
                cv2.rectangle(img, (x - 5, y - 5),
                              (x + w + 5, y + h + 5),
                              (175, 0, 175), cv2.FILLED)
                cv2.putText(img, button.text, (x + 20, y + 65),
                            cv2.FONT_HERSHEY_PLAIN, 4,
                            (255, 255, 255), 4)

                # Find distance between index and middle finger
                x1, y1 = lmList[8][:2]   # index finger tip
                x2, y2 = lmList[5][:2]  #knuckle
                x3, y3 = lmList[4][:2]     # thumb finger tip
                dist_knuckle = math.hypot(x2 - x1, y2 - y1)
                dist_thumb   = math.hypot(x3 - x1, y3 - y1)

                # If clicked

                if (dist_knuckle < 30 or dist_thumb < 50) and not pinched:
                    pinched=True
                    
                    if button.text == "<--":   # Backspace key
                        finalText = finalText[:-1]
                        keyboard.press(Key.backspace)
                    else:
                        finalText += button.text
                        keyboard.press(button.text)

                    cv2.rectangle(img, button.pos, (x + w, y + h), (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, button.text, (x + 20, y + 65),
                                cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
                elif dist_knuckle >= 40 and dist_thumb >= 50:
                    pinched = False

    # Display final text box
    cv2.rectangle(img, (50, 350), (700, 450),
                  (175, 0, 175), cv2.FILLED)
    cv2.putText(img, finalText, (60, 430),
                cv2.FONT_HERSHEY_PLAIN, 5,
                (255, 255, 255), 5)

    # Show image
    cv2.imshow("Image", img)
    cv2.waitKey(1)
