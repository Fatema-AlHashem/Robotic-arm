from ultralytics import YOLO 

#loads yolo trained model , best.pt contains the weights.

model=YOLO ('model/best.pt') #

#infrenece on the frame ()

def Get_detect(frame):
    results = model(frame) # infrence [x,y ], and conf score x-min/max ,y-min/max
    return results




