import cv2
import os

video_path = 'image/TAS.mp4'
output_dir = 'dataset/images/raw'
os.makedirs(output_dir, exist_ok=True)

cap = cv2.VideoCapture(video_path)
frame_count = 0
save_every = 30  # 每 30 幀存一張

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    if frame_count % save_every == 0:
        filename = os.path.join(output_dir, f'frame_{frame_count:05d}.jpg')
        cv2.imwrite(filename, frame)
    frame_count += 1

cap.release()
print('Done!')