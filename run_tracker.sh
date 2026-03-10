#!/bin/bash
set -e
pip install --upgrade setuptools packaging
source /opt/ros/humble/setup.bash
rm -rf build install log
colcon build
source install/setup.bash
ros2 launch ball_tracker ball_tracker.launch.py
