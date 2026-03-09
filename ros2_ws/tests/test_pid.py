from ros2_ws.src.ball_tracker.ball_tracker.pid_controller import PIDController

def test_pid_initialization():
    pid = PIDController(kp=1.0, ki=0.5, kd=0.1, max_output=5.0)
    assert pid.kp == 1.0
    assert pid.ki == 0.5
    assert pid.kd == 0.1
    assert pid.max_output == 5.0

def test_pid_proportional_only():
    pid = PIDController(kp=2.0, ki=0.0, kd=0.0, max_output=10.0)
    # 2.0 * 3.0 = 6.0
    output = pid.compute(current_error=3.0)
    assert output == 6.0

def test_pid_max_output_limit():
    pid = PIDController(kp=5.0, ki=0.0, kd=0.0, max_output=10.0)
    # 5.0 * 3.0 = 15.0 -> should be clamped to 10.0
    output = pid.compute(current_error=3.0)
    assert output == 10.0

def test_pid_derivative():
    pid = PIDController(kp=0.0, ki=0.0, kd=1.0, max_output=10.0)
    output1 = pid.compute(current_error=2.0)
    assert output1 == 2.0  # (2.0 - 0.0) * 1.0

    output2 = pid.compute(current_error=2.0)
    assert output2 == 0.0  # (2.0 - 2.0) * 1.0
