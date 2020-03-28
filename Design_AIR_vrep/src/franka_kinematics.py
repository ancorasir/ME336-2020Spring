import scipy.optimize
import numpy as np
from numpy import cos, sin


class HomeMatrix():
    '''
    Homegenous Matrix
    
    Parameter
    ------
        H: np.ndarray
    '''
    def __init__(self, H):
        self.data = H

    def rotation_part(self):
        return self.data[0:3,0:3]

    def transition_part(self):
        return self.data[0:3,3]

    def __mul__(self,H):
        return self.data @ H.data

class FrankaKinematics():
    '''
    provide Fk and IK function of franka panda
    '''
    def __init__(self):
        '''
        init some constants
        '''
        self.DH_parameter_list = {
            'j1':       {'a':0,         'd':0.333,  'alp':0},
            'j2':       {'a':0,         'd':0,      'alp':-np.pi/2},
            'j3':       {'a':0,         'd':0.316,  'alp':np.pi/2},
            'j4':       {'a':0.0825,    'd':0,      'alp':np.pi/2},
            'j5':       {'a':-0.0825,   'd':0.384,  'alp':-np.pi/2},
            'j6':       {'a':0,         'd':0,      'alp':np.pi/2},
            'j7':       {'a':0.088,     'd':0,      'alp':np.pi/2},
            'flange':   {'a':0,         'd':0.107,  'alp':0}, # theta = 0
            'gripper':  {'a':0,         'd':0.1034, 'alp':0}  # theta = 0
        }
        self.home_joint = (0, -np.pi/4, 0, -3 * np.pi/4, 0, np.pi/2, np.pi/4)
        self.joint_bonds = ((2.8973, 1.7628,2.8973,-0.0698,2.8973,3.7525,2.8973),
                            (-2.8973, -1.7628, -2.8973, -3.0718, -2.8973, -0.0175, -2.8973))

    def dh_home_matrix(self,theta,d,a,alp)->HomeMatrix:
        '''
        Hx_x+1 = Rot_Z_theta * Trans_Z_d * Trans_X_a * Rot_X_alp
        
        c_theta         -s_theta*c_alp  s_theta*s_alp       a*c_theta

        s_theta         c_theta*c_alp   -c_theta*s_alp      a*s_theta

        0               s_alp           c_alp               d

        0               0               0                   1
        '''
        c_theta = cos(theta)
        s_theta = cos(theta)
        c_alp = cos(alp)
        s_alp = sin(alp)
        return HomeMatrix(np.array([
            [c_theta         ,-s_theta*c_alp  ,s_theta*s_alp       ,a*c_theta],
            [s_theta         ,c_theta*c_alp   ,-c_theta*s_alp      ,a*s_theta],
            [0               ,s_alp           ,c_alp               ,d],
            [0               ,0               ,0                   ,1]
        ]))
    
    def fk(self, q):
        '''
        forward kenimatics of panda
        compute Homegenous Matrix form joint angle
        H = H0_1 * H1_2 * H2_3 * H3_4 * H4_5 * H5_6 * H6_7 * H_flange * H_gripper
        '''
        
        # check q
        if type(q) != type(np.array(0)) or q.shape[0] != 7:
            raise ValueError('q should be (np.ndarray) and (7) length')

        # H = H0_1 * H1_2 * H2_3 * H3_4 * H4_5 * H5_6 * H6_7
        H = HomeMatrix(np.eye(4))
        for i, theta in enumerate(q):
            DH_parameter = self.DH_parameter_list[i]
            H = H @ self.dh_home_matrix(theta, DH_parameter['d'], DH_parameter['a'], DH_parameter['alp'])

        # H = H * H_flange * H_gripper
        H = H

    def ik(self, H_target: HomeMatrix, H_guess: HomeMatrix):
        pass

if __name__ == "__main__":
    a = np.random.rand(4,4)
    print(a)
    H1 = HomeMatrix(a)
    print(H1.rotation_part(), H1.transition_part())