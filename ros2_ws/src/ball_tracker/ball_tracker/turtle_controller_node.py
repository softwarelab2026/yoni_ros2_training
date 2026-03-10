import math
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, Point
from turtlesim.msg import Pose
from ball_tracker.pid_controller import PIDController


class TurtleController(Node):
    def __init__(self):
        super().__init__("turtle_controller_node")

        self._cmd_vel_publisher = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self._pose_subscriber = self.create_subscription(
            Pose, "/turtle1/pose", self._pose_callback, 10
        )

        self._target_subscriber = self.create_subscription(
            Point, "/target_point", self._target_callback, 10
        )

        self._linear_pid = PIDController(kp=5.0, ki=0.0, kd=0.0, max_output=10.0)
        self._angular_pid = PIDController(kp=5.0, ki=0.0, kd=0.0, max_output=10.0)

        self._turtle_pose = None
        self._target_point = None

        self._timer = self.create_timer(0.1, self._control_loop)

    def _pose_callback(self, msg):
        self._turtle_pose = msg

    def _target_callback(self, msg):
        self._target_point = msg
        self.get_logger().info(f"Target updated: X={msg.x:.2f}, Y={msg.y:.2f}")

    def _control_loop(self):
        if self._turtle_pose is None or self._target_point is None:
            return

        dx = self._target_point.x - self._turtle_pose.x
        dy = self._target_point.y - self._turtle_pose.y
        distance = math.sqrt(dx**2 + dy**2)

        if distance < 0.1:
            self._cmd_vel_publisher.publish(Twist())
            self.get_logger().info(
                f"Target reached: X={self._target_point.x:.2f}, Y={self._target_point.y:.2f}"
            )
            return

        angle_to_target = math.atan2(dy, dx)
        angle_error = angle_to_target - self._turtle_pose.theta
        angle_error = math.atan2(math.sin(angle_error), math.cos(angle_error))

        angular_vel = self._angular_pid.compute(
            setpoint=0.0, measured_value=-angle_error, dt=0.1
        )
        linear_vel = self._linear_pid.compute(
            setpoint=0.0, measured_value=-distance, dt=0.1
        )

        cmd_msg = Twist()
        cmd_msg.linear.x = linear_vel
        cmd_msg.angular.z = angular_vel
        self._cmd_vel_publisher.publish(cmd_msg)


def main(args=None):
    rclpy.init(args=args)
    node = TurtleController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
