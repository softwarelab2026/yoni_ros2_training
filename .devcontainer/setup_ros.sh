#!/bin/bash
cd ros2_ws/
colcon build --symlink-install
echo 'source /opt/ros/humble/setup.bash' >> ~/.bashrc
echo 'source /workspaces/yoni_ros2_training/ros2_ws/install/setup.bash' >> ~/.bashrc
