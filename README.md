# pymavlink_tutorial
This repository contains different pymavlink tutorial tryouts and experimental projects 

Prerequisitory Steps:
  1. Setting up SITL
      - https://ardupilot.org/dev/docs/setting-up-sitl-on-linux.html
      - https://ardupilot.org/dev/docs/sitl-simulator-software-in-the-loop.html#sitl-simulator-software-in-the-loop
      - Refer to the two links above; starting the "sim_vehicle.py" software can be done in the ardupilot/Tools/autotest/ directory, not the one stated in         the first link under "Start SITL simulator". 
      - To add a little side note, the ardupilot repository for SITL may cause issues when you try to put it under your own repository. By any chance you           tried adding this separate git repository to your own, which I hope is really not the case, you can undo this process by the following process.
        
        a. Remove the repository within your own.
        
        b. Open .profile with a text editor. The file should be in your home directory. At the bottom of this file, there should be a bunch of file                    directories defined; remove those that contain your git repository and the ardupilot ones mixed up.
        
        c. Open .bashrc and scroll down to the bottom of this script as well. You should see similar directory definitions there; remove those that contain            a mixup of your git repository and the ardupilot git repository.
      
  3. Setting up QGroundControl
      - https://docs.qgroundcontrol.com/master/en/getting_started/download_and_install.html
      - Follow the steps in the link above; it's a set of straight forward commands. Shouldn't be too complicated.
  
  5. Preparing Python dependency
      - run pip3(pip) install pymavlink
