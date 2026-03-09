import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import cv2
from cv_bridge import CvBridge
import numpy as np


class BallTracker(Node):
    def __init__(self):
        super().__init__("ball_tracker_node")

        self._publisher = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)

        self._subcription = self.create_subscription(
            Image, "/camera/image_raw", self._image_callback, 10
        )

        self._pose_subscriber = self.create_subscription(
            Pose, "/turtle1/pose", self._pose_callback, 10
        )

        self.turtle_x = 0.0
        self.turtle_y = 0.0
        self.turtle_theta = 0.0

        self.bridge = CvBridge()
        self.ball_pixel_x = 0.0
        self.ball_pixel_y = 0.0

        self.target_x = 0.0
        self.target_y = 0.0

    def _pixels_to_turtlesim(self, pixel_x, pixel_y):
        sim_x = (pixel_x / 500.0) * 11.0
        sim_y = ((500.0 - pixel_y) / 500.0) * 11.0
        return sim_x, sim_y

    def _pose_callback(self, msg):
        self.turtle_x = msg.x
        self.turtle_y = msg.y
        self.turtle_theta = msg.theta

    def _image_callback(self, msg):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")

            lower_red = np.array([0, 0, 200])
            upper_red = np.array([50, 50, 255])

            red_mask = cv2.inRange(cv_image, lower_red, upper_red)

            M = cv2.moments(red_mask)
            if M["m00"] > 0:
                self.ball_pixel_x = int(M["m10"] / M["m00"])
                self.ball_pixel_y = int(M["m01"] / M["m00"])

                self.target_x, self.target_y = self._pixels_to_turtlesim(
                    self.ball_pixel_x, self.ball_pixel_y
                )

                self.get_logger().info(
                    f"target -> X: {self.target_x:.2f}m, Y: {self.target_y:.2f}m"
                )
            else:
                self.get_logger().info("no ball in frame..")

        except Exception as e:
            self.get_logger().error(f"Camera error: {e}")


def main(args=None):
    rclpy.init(args=args)
    ball_tracker = BallTracker()
    rclpy.spin(ball_tracker)
    ball_tracker.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
