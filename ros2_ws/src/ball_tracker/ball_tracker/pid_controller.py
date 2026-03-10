class PIDController:
    def __init__(self, kp, ki, kd, max_output=2.0):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.max_output = max_output

        self.integral_sum = 0.0
        self.previous_error = 0.0

    def _clamp(self, value, limit):
        return max(min(value, limit), -limit)

    def compute(self, setpoint, measured_value, dt=0.1):
        current_error = setpoint - measured_value

        p_term = self.kp * current_error

        self.integral_sum += current_error * dt
        self.integral_sum = self._clamp(self.integral_sum, self.max_output)
        i_term = self.ki * self.integral_sum

        derivative = (current_error - self.previous_error) / dt
        d_term = self.kd * derivative

        self.previous_error = current_error

        total_output = p_term + i_term + d_term
        return self._clamp(total_output, self.max_output)
