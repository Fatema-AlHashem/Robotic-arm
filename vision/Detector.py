from ultralytics import YOLO 

#loads yolo trained model 

model=YOLO ('yolov8n.pt') #replace with best.pt

#infrenece on the frame ()

def Get_detect(frame):
    results = model(frame) # infrence [x,y ], and conf score x-min/max ,y-min/max
    return results



