import cv2
from pathlib import Path
import numpy as np

SEGUNDO = 534

cap = cv2.VideoCapture(str(Path("data") / "videos" / "video.mp4"))
ANCHO_REF, ALTO_REF = 1920, 1080

fps = cap.get(cv2.CAP_PROP_FPS)
nro_frames = int(SEGUNDO * fps)

cap.set(cv2.CAP_PROP_POS_FRAMES, nro_frames)
ret, frame = cap.read()
cap.release()

if ret:
    frame = cv2.resize(frame, (ANCHO_REF, ALTO_REF))
    cv2.imwrite(str(Path("data") / "images" / "frame_test_534s.png"), frame)
    print(f"Frame saved successfully at {nro_frames} : {SEGUNDO}s.")
else:   
    print("Failed to read the frame.")

alto, ancho = frame.shape[:2]
x1 = int(ancho * 0.65)
y1 = int(alto * 0.05)
x2 = ancho
y2 = int(alto * 0.30)

killfeed = frame[y1:y2, x1:x2]
cv2.imwrite(str(Path("data") / "images" / "killfeed_cropped.png"), killfeed)
print(f"killfeed cropped: {killfeed.shape[1]}x{killfeed.shape[0]}")

killfeed_hsv = cv2.cvtColor(killfeed, cv2.COLOR_BGR2HSV)

verde_bajo = np.array([60, 60, 130])
verde_alto = np.array([85, 140, 220])

mascara = cv2.inRange(killfeed_hsv, verde_bajo, verde_alto)
pixeles_verdes = cv2.countNonZero(mascara)

print(f"Píxeles verdes detectados: {pixeles_verdes}")
cv2.imwrite(str(Path("data") / "images" / "mascara_verde.png"), mascara)