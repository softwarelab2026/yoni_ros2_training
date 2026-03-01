from rclpy.node import Node
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist

class BallTracker(Node):
    def __init__(self):
        super().__init__('ball_tracker_node')

        self._publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

        self._subcription = self.create_subscription(
            Image,
            'camera/image_raw',
            self._image_callback,
            10
        )

    def _image_callback(self, msg):
        # ball tracking logic
        pass