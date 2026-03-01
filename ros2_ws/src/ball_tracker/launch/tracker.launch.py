from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='sim'
        ),
        Node(
            package='ball_tracker',
            executable='virtual_camera_node',
            name='camera'
        ),
        Node(
            package='ball_tracker',
            executable='ball_tracker_node',
            name='tracker'
        )
    ])