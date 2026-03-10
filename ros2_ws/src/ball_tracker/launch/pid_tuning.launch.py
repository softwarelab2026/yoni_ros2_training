from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription(
        [
            Node(package="turtlesim", executable="turtlesim_node", name="sim"),
            Node(
                package="ball_tracker",
                executable="turtle_controller_node",
                name="controller",
            ),
            Node(package="rqt_gui", executable="rqt_gui", name="interface"),
        ]
    )
