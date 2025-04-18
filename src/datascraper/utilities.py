from ultralytics import YOLO
from roboflow import Roboflow
import numpy as np
import h5py

"""
Module currently in progress.
"""

def load_moves_from_HDF5(source):
    with h5py.File(source, "r") as of:
        move_sequence = of["moves"][:]
    
    return move_sequence

"""
def retrain_vision_model():
    model = YOLO('yolo11m.pt')  # load a pretrained model (recommended for training)
    model.to('cuda')
    model.train(data='./../../datasets/hold_image_datasets/data.yaml', 
                epochs=100, 
                imgsz=(640, 640), 
                batch = 4
                )  
"""

"""
def retrain_pose_model():
    model = YOLO('yolov8m-pose.pt')  # load a pretrained model (recommended for training)
    model.to('cuda')
    model.train(data='./../../datasets/posedatasets2/data.yaml', 
                    epochs=100, 
                    imgsz=(640, 640))
    
def gaussian(x,mean,sigma):
    return 1/np.sqrt(2*np.pi*sigma**2)*np.exp(-(x-mean)/(2*sigma**2))
"""

