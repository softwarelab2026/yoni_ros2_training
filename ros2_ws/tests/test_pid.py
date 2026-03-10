from src.ball_tracker.ball_tracker.pid_controller import PIDController


def test_pid_initialization():
    pid = PIDController(kp=1.0, ki=0.5, kd=0.1, max_output=5.0)
    assert pid.kp == 1.0
    assert pid.ki == 0.5
    assert pid.kd == 0.1
    assert pid.max_output == 5.0


def test_pid_proportional_only():
    pid = PIDController(kp=2.0, ki=0.0, kd=0.0, max_output=10.0)
    output = pid.compute(setpoint=3.0, measured_value=0.0)
    assert output == 6.0


def test_pid_max_output_limit():
    pid = PIDController(kp=5.0, ki=0.0, kd=0.0, max_output=10.0)
    output = pid.compute(setpoint=3.0, measured_value=0.0)
    assert output == 10.0


def test_pid_derivative_with_dt():
    pid = PIDController(kp=0.0, ki=0.0, kd=1.0, max_output=100.0)

    output = pid.compute(setpoint=2.0, measured_value=0.0, dt=0.1)
    assert output == 20.0


def test_pid_integral_and_anti_windup():
    pid = PIDController(kp=0.0, ki=1.0, kd=0.0, max_output=5.0)

    output1 = pid.compute(setpoint=10.0, measured_value=0.0, dt=0.1)
    assert output1 == 1.0

    output2 = pid.compute(setpoint=100.0, measured_value=0.0, dt=1.0)
    assert output2 == 5.0
