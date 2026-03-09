class PIDController:
    def __init__(self, kp, ki, kd, max_output=2.0):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.max_output = max_output
        
        self.integral_sum = 0.0
        self.previous_error = 0.0
