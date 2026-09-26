import cv2
from pathlib import Path

img = cv2.imread(str(Path("data") / "images" / "frame_test_49s.png"))  # o el frame que tengas
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

clicked = []

def click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        pixel_bgr = img[y, x]
        pixel_hsv = hsv[y, x]
        print(f"Pos ({x},{y}) -> BGR: {pixel_bgr} | HSV: {pixel_hsv}")

cv2.namedWindow("Click en el verde del banner 'Me'")
cv2.setMouseCallback("Click en el verde del banner 'Me'", click)

while True:
    cv2.imshow("Click en el verde del banner 'Me'", img)
    if cv2.waitKey(1) == 27:  # ESC para salir
        break

cv2.destroyAllWindows()