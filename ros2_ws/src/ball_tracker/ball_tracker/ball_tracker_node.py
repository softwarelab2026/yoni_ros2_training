import rclpy
from rclpy.node import Node
from ball_tracker.geometry import pixels_to_turtlesim
from sensor_msgs.msg import Image
from geometry_msgs.msg import Point
import cv2
from cv_bridge import CvBridge
import numpy as np


class BallTracker(Node):
    def __init__(self):
        super().__init__("ball_tracker_node")

        self._target_publisher = self.create_publisher(Point, "/target_point", 10)

        self._image_subscriber = self.create_subscription(
            Image, "/camera/image_raw", self._image_callback, 10
        )

        self._bridge = CvBridge()

    def _image_callback(self, msg):
        try:
            cv_image = self._bridge.imgmsg_to_cv2(msg, "bgr8")

            lower_red = np.array([0, 0, 200])
            upper_red = np.array([50, 50, 255])
            red_mask = cv2.inRange(cv_image, lower_red, upper_red)

            M = cv2.moments(red_mask)
            if M["m00"] > 0:
                ball_pixel_x = int(M["m10"] / M["m00"])
                ball_pixel_y = int(M["m01"] / M["m00"])

                target_x, target_y = pixels_to_turtlesim(ball_pixel_x, ball_pixel_y)

                target_msg = Point()
                target_msg.x = target_x
                target_msg.y = target_y
                self._target_publisher.publish(target_msg)

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
