import cv2
from pathlib import Path
SEGUNDO = 49

cap = cv2.VideoCapture(str(Path("data") / "videos" / "video.mp4"))
ANCHO_REF, ALTO_REF = 1920, 1080

fps = cap.get(cv2.CAP_PROP_FPS)
nro_frames = int(SEGUNDO * fps)

cap.set(cv2.CAP_PROP_POS_FRAMES, nro_frames)
ret, frame = cap.read()
cap.release()

if ret:
    frame = cv2.resize(frame, (ANCHO_REF, ALTO_REF))
    cv2.imwrite(str(Path("data") / "images" / "frame_test_49s.png"), frame)
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

template = cv2.imread(str(Path("data") / "images" / "kill_template.png"), cv2.IMREAD_GRAYSCALE)
if template is None:
    raise FileNotFoundError("Template image not found. Please check the path.") #no ejecutar lo siguiente

cv2.imwrite(str(Path("data") / "images" / "killfeed_zoom.png"), 
            cv2.resize(killfeed, None, fx=3, fy=3, interpolation=cv2.INTER_NEAREST))

killfeed_gris = cv2.cvtColor(killfeed, cv2.COLOR_BGR2GRAY)

resultado = cv2.matchTemplate(killfeed_gris, template, cv2.TM_CCOEFF_NORMED)
_, confianza, _, ubicacion = cv2.minMaxLoc(resultado)
                                           
print(f"Confianza: {confianza:.2f}, Ubicación: {ubicacion}")

# TODO: Implementar ahora la lógica para ver si da mejores valores por hsv (color)