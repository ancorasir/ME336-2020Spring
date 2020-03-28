# How to install v-rep and pyrep
Altough we use these two software at same time, but they are independent software. We can install them separately.

prerequest: Ubuntu; Python3.6 or higher; Git; 
## Install v-rep

V-rep now has a new name: *coppeliaSim*, but still the same thing

- Visit v-rep Downloads web page: [https://www.coppeliarobotics.com/ubuntuVersions](https://www.coppeliarobotics.com/ubuntuVersions).

- Click to download the *Edu* package depends on your system version(16.04 or 18.04)
![](downloads_webpage.png)

- Extract the zip file into a directory you want

- Test: open terminal in the directory, then run the        following command to open v-rep.
    ```bash
    $ ./coppeliaSim.sh
    ```
    if no warning occur, all finished

## Install pyrep  

```bash
$ cd THE/PATH/YOU/WANT
$ git clone https://github.com/stepjam/PyRep.git
$ cd PyRep
``` 
Add the following to your ~/.bashrc file: (NOTE: the 'EDIT ME' in the first line)
```
export COPPELIASIM_ROOT=EDIT/ME/PATH/TO/COPPELIASIM/INSTALL/DIR
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$COPPELIASIM_ROOT
export QT_QPA_PLATFORM_PLUGIN_PATH=$COPPELIASIM_ROOT
```
Remember to source your bashrc (source ~/.bashrc) or zshrc (source ~/.zshrc) after this.
```bash
$ pip3 install -r requirements.txt
$ python3 setup.py install --user
```
Test:
```bash
$ cd examples
$ python3 example_panda_reach_target.py
```