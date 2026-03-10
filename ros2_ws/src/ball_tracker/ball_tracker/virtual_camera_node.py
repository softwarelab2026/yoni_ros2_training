import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np


class VirtualCamera(Node):
    def __init__(self):
        super().__init__("virtual_camera_node")

        self.publisher_ = self.create_publisher(Image, "/camera/image_raw", 10)

        self.timer = self.create_timer(0.1, self.timer_callback)

        self.br = CvBridge()

        self.x = 250
        self.y = 250
        self.dx = 3
        self.dy = 3
        self.radius = 20

    def timer_callback(self):
        frame = np.zeros((500, 500, 3), dtype=np.uint8)

        self.x += self.dx
        self.y += self.dy

        if self.x <= self.radius or self.x >= 500 - self.radius:
            self.dx *= -1
        if self.y <= self.radius or self.y >= 500 - self.radius:
            self.dy *= -1

        cv2.circle(frame, (self.x, self.y), self.radius, (0, 0, 255), -1)

        cv2.imshow("Virtual Camera Feed", frame)
        cv2.waitKey(1)

        msg = self.br.cv2_to_imgmsg(frame, encoding="bgr8")
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    virtual_camera = VirtualCamera()
    rclpy.spin(virtual_camera)
    virtual_camera.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
