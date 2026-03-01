#!/bin/bash
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
echo "cd ros2_ws/ && colcon build" >> ~/.bashrc
echo "source install/setup.bash" >> ~/.bashrc