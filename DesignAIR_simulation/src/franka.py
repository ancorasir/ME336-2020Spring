from pyrep.robots.arms.panda import Panda
from pyrep.robots.configuration_paths.arm_configuration_path import ArmConfigurationPath
from typing import List, Union
import numpy as np
from scipy.optimize import minimize
import franka_kinematics

class Franka(Panda):

    def __init__(self):
        super().__init__()

    def get_linear_path(self, position: Union[List[float], np.ndarray],
                        euler: Union[List[float], np.ndarray] = None,
                        quaternion: Union[List[float], np.ndarray] = None,
                        steps=50, ignore_collisions=False
                        ) -> ArmConfigurationPath:
        pass
    def get_nonlinear_path(self, position: Union[List[float], np.ndarray],
                           euler: Union[List[float], np.ndarray] = None,
                           quaternion: Union[List[float], np.ndarray] = None,
                           ignore_collisions=False,
                           trials=100, max_configs=60, trials_per_goal=6,
                           algorithm=None) -> ArmConfigurationPath:
        pass                   
    def get_path(self, position: Union[List[float], np.ndarray],
                 euler: Union[List[float], np.ndarray] = None,
                 quaternion: Union[List[float], np.ndarray] = None,
                 ignore_collisions=False,
                 trials=100, max_configs=60, trials_per_goal=6,
                 algorithm=None) -> ArmConfigurationPath:
        pass         