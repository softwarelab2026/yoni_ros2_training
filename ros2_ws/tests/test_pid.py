from ros2_ws.build.ball_tracker.ball_tracker.pid_controller import PIDController

def test_pid_initialization():
    pid = PIDController(kp=1.0, ki=0.5, kd=0.1, max_output=5.0)
    assert pid.kp == 1.0
    assert pid.ki == 0.5
    assert pid.kd == 0.1
    assert pid.max_output == 5.0
