import sys
import cv2
import os
from sys import platform

dir_path = os.path.dirname(os.path.realpath(__file__))
if platform == "win32": sys.path.append(dir_path + '\\..\\..\\python\\openpose\\');
else: sys.path.append('..\\..\\python');

try:
    from openpose import *
except:
    raise Exception('Error: OpenPose library could not be found. Did you enable `BUILD_PYTHON` in CMake and have this Python script in the right folder?')
params = dict()
params["logging_level"] = 3
params["output_resolution"] = "-1x-1"
params["net_resolution"] = "320x172"
params["model_pose"] = "COCO"
params["alpha_pose"] = 0.6
params["scale_gap"] = 0.3
params["scale_number"] = 1
params["render_threshold"] = 0.05
params["render_pose"] = 1
params["num_gpu_start"] = 0
params["disable_blending"] = False
params["default_model_folder"] = dir_path + "\\..\\..\\models\\"
openpose = OpenPose(params)

while 1:
    frame = cv2.imread(-1)
    keypoints, output_image = openpose.forward(frame, True)
    rf = keypoints['right_foot']
    rh = keypoints['right hand']
    if ((rf.x-rh.x)^2+(rf.y-rh.y)^2)^0.5<13.4:
        print('Downward dog is done correctly')
    else:
        print('Downward dog is not done correctly.')
    
    cv2.imshow("output", output_image)
    cv2.waitKey(15)
