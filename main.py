import cv2

SEGUNDO = 49

cap =  cv2.VideoCapture("data/videos/video.mp4")

fps = cap.get(cv2.CAP_PROP_FPS)
nro_frames = int(SEGUNDO * fps)

cap.set(cv2.CAP_PROP_POS_FRAMES, nro_frames)
ret, frame = cap.read()
cap.release()

if ret:
    cv2.imwrite("data/images/frame_test_49s.png", frame)
    print(f"Frame saved successfully at {nro_frames} : {SEGUNDO}s.")
else:   
    print("Failed to read the frame.")