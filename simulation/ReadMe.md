# Simulation

## File Structure

- scene : ".ttt" v-rep scene files
- src: backend python code put here
- tasks:
  - BaseScene_test:test scene file and backend code
  - Kine_picking: simulate kinematic picking 

## Getting Start

prerequest: PyRep
  
```bash
$ cd simulation/tasks/THE_TASK_YOU_WANT_TO_RUN
$ python3 main.py
```

## Basic Usage of simulation

import

``` python
from src.camera import Camera
from src.env import Env
from src.franka import Franka
```

Env

```python
# build Env
env = Env('path to .ttt file')
# start simulation
env.start()
# stop simulation
env.stop()
# shatdown the v-rep GUI thread
env.shutdown()
```

Camera

```python
# build Camera
cam = Camera()
# capture BGR image
img = cam.capture_bgr()
# capture Depth
depth = cam.capture_depth(in_meters=True)
```

Robot

```python
# build franka
franka = Franka()
# move
franka.move(env,position,euler=euler)
# home
franka.home(env)
```
