#!/bin/bash
set -e

source /opt/ros/humble/setup.bash
source /workspace/ros2_ws/install/setup.bash

ros2 launch ball_tracker ball_tracker.launch.py
