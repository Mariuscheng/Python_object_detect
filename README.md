# 遊戲影片物件偵測專案

本專案利用 Ultralytics YOLO（支援 YOLOv8/YOLOv11/YOLOv12）進行遊戲影片的物件偵測。

## 功能簡介
- 從遊戲影片（如 TAS.mp4）擷取圖片並標註
- 使用 Roboflow 或 LabelImg 製作自訂資料集
- 訓練 YOLO 模型（支援 GPU/CPU）
- 將訓練好的模型應用於影片推論，產生標註後的新影片
- 可選擇不同大小的 YOLO 模型（n/s/m/l/x）以平衡速度與準確率

## 適用場景
- 遊戲影片自動分析
- 遊戲角色、道具、敵人等自訂物件偵測
- AI 影片標註輔助

## 主要技術
- Python 3.12
- Ultralytics YOLOv8/YOLOv11/YOLOv12
- OpenCV
- Roboflow（資料集標註與管理）

---
如需訓練、推論或資料集準備教學，請參考專案內說明或聯絡作者。
