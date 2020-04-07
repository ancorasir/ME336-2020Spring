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
import numpy as np
import cv2

def scene(scene_file_name):
    '''
    return abs dir of scene file 
    '''
    return scene_path + scene_file_name
if __name__ == '__main__':
    # open v-rep and launch BaseScene.ttt file
    env = Env(scene('Kine_picking.ttt'))
    # start simulation
    # env.set_simulation_timestep(0.1)
    # env.step_ui()
    env.start()

    # franka
    franka = Franka()
    # set franka to home joints 
    franka.home(env)
    
    # cam 
    cam = Camera()
    '''
    # target_plane, cylinder, cubic 
    target_plane = Shape('plane')
    cubic = Shape('obj0')
    cylinder = Shape('obj1')

    obj = cubic

    # franka move above the object
    obj_position = obj.get_position()
    obj_position[2] += 0.1
    input('Press enter to move above the object')
    franka.move(env,obj_position,euler=[0,np.radians(180),0])

    # approch the object
    obj_position[2] -= 0.1
    input('Press enter to approch the object')
    franka.move(env,obj_position,euler=[0,np.radians(180),0])
    
    # grasp the object
    input('Press enter to grasp the object')
    franka.grasp(env,obj)
    
    # lift the object
    obj_position[2] += 0.1
    input('Press enter to lift the object')
    franka.move(env,obj_position,euler=[0,np.radians(180),0])
    
    # transport the object to target position
    target_plane_position = target_plane.get_position()
    target_plane_position[2] += 0.1
    input('Press enter to transport the object to target position')
    franka.move(env,target_plane_position,euler=[0,np.radians(180),0])
    '''
    # TODO: generate a path looks like the letters in "COVID-19"
    x,y,z = franka.get_position()
    '''
    rotate along Y axis 45 degrees
    and move to robot frame
    '''
    rotation = np.array([
        [np.cos(np.pi/4),0,np.sin(np.pi/4),x],
        [0,1,0,y],
        [-np.sin(np.pi/4),0,np.cos(np.pi/4),z],
        [0,0,0,1]
    ])
    '''
    letter_range

      0.4
    -------
    |     |
    |  *  | 0.2 ----> y
    |     |
    -------
       |
       |
       | x

    z = 0.7
    
    letter_range=[
        [-0.2,0.1,0.7,1],
        [-0.2,-0.1,0.7,1],
        [0.2,-0.1,0.7,1],
        [0.2,0.1,0.7,1],
        [-0.2,0.1,0.7,1]
    ]
    '''
    letter_c_targets = [
        [-0.1,0.1,0.7,1],
        [-0.2,0,0.7,1],
        [-0.1,-0.1,0.7,1],
        [0.1,-0.1,0.7,1],
        [0.2,0,0.7,1],
        [0.1,0.1,0.7,1]
    ]

    for i,p in enumerate(letter_c_targets):
        if(i==0):
            franka.clear_path = True
        else:
            franka.clear_path = False
        rp = rotation@np.array(p)
        franka.move(env,rp[:3],euler=[0,np.radians(180),0])
    franka.home(env)
    env.stop()
    env.shutdown()