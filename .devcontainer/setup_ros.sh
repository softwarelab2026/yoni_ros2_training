#!/bin/bash
cd ros2_ws/
colcon build --symlink-install
echo 'alias sros="source /opt/ros/humble/setup.bash && source ros2_ws/install/setup.bash"' >> ~/.bashrc
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
