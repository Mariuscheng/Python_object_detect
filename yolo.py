from ultralytics import YOLO

model = YOLO('yolov8x')

model.predict('image/image.png', save=True)