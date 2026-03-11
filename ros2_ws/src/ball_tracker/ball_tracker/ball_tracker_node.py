import cv2
import numpy as np
import rclpy
from cv_bridge import CvBridge
from geometry_msgs.msg import Point
from rclpy.node import Node
from sensor_msgs.msg import Image

from ball_tracker.geometry import convert_camera_pixels_to_turtlesime_corrdinates


class BallTracker(Node):
    def __init__(self):
        super().__init__("ball_tracker_node")

        self._target_publisher = self.create_publisher(Point, "/target_point", 10)
        self._image_subscriber = self.create_subscription(Image, "/camera/image_raw", self._image_callback, 10)
        self._bridge = CvBridge()

    def _find_center_of_mass(self, mask):
        M = cv2.moments(mask)
        if M["m00"] > 0:
            ball_pixel_x = int(M["m10"] / M["m00"])
            ball_pixel_y = int(M["m01"] / M["m00"])
            return ball_pixel_x, ball_pixel_y
        return None, None

    def _image_callback(self, msg):
        try:
            cv_image = self._bridge.imgmsg_to_cv2(msg, "bgr8")

            lower_red = np.array([0, 0, 200])
            upper_red = np.array([50, 50, 255])
            red_mask = cv2.inRange(cv_image, lower_red, upper_red)

            ball_pixel_x, ball_pixel_y = self._find_center_of_mass(red_mask)

            if ball_pixel_x is not None and ball_pixel_y is not None:
                target_x, target_y = convert_camera_pixels_to_turtlesime_corrdinates(ball_pixel_x, ball_pixel_y)

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
