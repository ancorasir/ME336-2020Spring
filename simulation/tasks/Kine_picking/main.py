'''
Kinematic picking
'''
from os.path import dirname, abspath
sim_path = dirname(dirname(dirname(abspath(__file__))))
scene_path = sim_path + '/scene/'
import sys
sys.path.append(sim_path)
from src.camera import Camera
from src.env import Env
from src.franka import Franka
from pyrep.objects.shape import Shape
from pyrep.const import PrimitiveShape
import numpy as np
import cv2

