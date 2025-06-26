from ultralytics import YOLO
import torch

if __name__ == "__main__":
    # 載入預訓練模型
    model = YOLO('yolo11m.pt')

    # 訓練模型，請確認 data 路徑正確
    model.train(data='dataset/data.yaml', epochs=50, device="0")

    print(torch.cuda.is_available())
    print(torch.cuda.get_device_name(0) if torch.cuda.is_available() else "No GPU")
