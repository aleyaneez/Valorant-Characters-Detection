from ultralytics import YOLO
import cv2 as cv

video_path = "test/sunset.mp4"
model_path = "best.pt"

model = YOLO(model_path)
cap = cv.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: No se pudo abrir el video.")
    exit()

fps = cap.get(cv.CAP_PROP_FPS)
total_frames = cap.get(cv.CAP_PROP_FRAME_COUNT)

delay = int(1000 / fps)


while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, conf=0.8)
    r = results[0]
    annotated = r.plot()

    cv.imshow("YOLO Best Medium", annotated)

    key = cv.waitKey(delay)

    if key & 0xFF == ord('q'):
        break
    
    elif key == 83: 
        current_frame = cap.get(cv.CAP_PROP_POS_FRAMES)
        saltar_a = current_frame + (5 * fps)
        cap.set(cv.CAP_PROP_POS_FRAMES, min(saltar_a, total_frames))

    elif key == 81:
        current_frame = cap.get(cv.CAP_PROP_POS_FRAMES)
        saltar_a = current_frame - (5 * fps)
        cap.set(cv.CAP_PROP_POS_FRAMES, max(saltar_a, 0))

cap.release()
cv.destroyAllWindows()