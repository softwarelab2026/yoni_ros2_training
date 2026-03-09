import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class BallTracker(Node):
    def __init__(self):
        super().__init__('ball_tracker_node')

        self._publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

        self._subcription = self.create_subscription(
            Image,
            '/camera/image_raw',
            self._image_callback,
            10
        )

        self._pose_subscriber = self.create_subscription(
            Pose,
            '/turtle1/pose',
            self._pose_callback,
            10
        )

        self.turtle_x = 0.0
        self.turtle_y = 0.0
        self.turtle_theta = 0.0

    def _pose_callback(self, msg):
        self.turtle_x = msg.x
        self.turtle_y = msg.y
        self.turtle_theta = msg.theta

    def _image_callback(self, msg):
        pass

def main(args=None):
    rclpy.init(args=args)
    ball_tracker = BallTracker()
    rclpy.spin(ball_tracker)
    ball_tracker.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()