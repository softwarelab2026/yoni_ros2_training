
# Yoantan ROS2 Training

## Overview
In this project, I built a Python ROS2 node that makes a robot in the Turtlesim simulator automatically follow a ball using image processing and a simple control approach.

## How It Works
The node subscribes to '/camera/image_raw' to receive camera images.
Using 'cv_bridge', I convert ROS image messages into OpenCV images.

Finally, the node publishes velocity commands to '/turtle1/cmd_vel', allowing the robot to move and follow the ball.