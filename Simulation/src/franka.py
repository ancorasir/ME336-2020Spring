from pyrep.robots.arms.panda import Panda
from pyrep.robots.configuration_paths.arm_configuration_path import ArmConfigurationPath
from pyrep.errors import ConfigurationError, ConfigurationPathError, IKError
from pyrep.const import ConfigurationPathAlgorithms as Algos
from typing import List, Union
import numpy as np
from scipy.optimize import minimize
import franka_kinematics

class Franka(Panda):

    def __init__(self):
        super().__init__()

    def _get_linear_path(self, position: Union[List[float], np.ndarray],
                        euler: Union[List[float], np.ndarray] = None,
                        quaternion: Union[List[float], np.ndarray] = None,
                        steps=50, ignore_collisions=False
                        ) -> ArmConfigurationPath:
        pass
        

    def _get_nonlinear_path(self, position: Union[List[float], np.ndarray],
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
                 algorithm=Algos.SBL
                 ) -> ArmConfigurationPath:
        try:
            p = self.get_linear_path(position, euler, quaternion,
                                     ignore_collisions=ignore_collisions)
            return p
        except ConfigurationPathError:
            pass  # Allowed. Try again, but with non-linear.
        
        try: 
            # TODO: _get_linear_path
            pass
        except ConfigurationError:
            pass

        # This time if an exception is thrown, we dont want to catch it.
        p = self.get_nonlinear_path(
            position, euler, quaternion, ignore_collisions, trials, max_configs,
            trials_per_goal, algorithm)
        return p