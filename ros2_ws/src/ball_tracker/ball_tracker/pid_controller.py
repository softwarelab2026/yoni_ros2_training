class PIDController:
    def __init__(self, kp, ki, kd, max_output=2.0):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.max_output = max_output

        self.integral_sum = 0.0
        self.previous_error = 0.0

    def compute(self, current_error):
        p_term = self.kp * current_error

        self.integral_sum += current_error
        self.integral_sum = max(min(self.integral_sum, 10.0), -10.0)
        i_term = self.ki * self.integral_sum

        derivative = current_error - self.previous_error
        d_term = self.kd * derivative

        self.previous_error = current_error

        total_output = p_term + i_term + d_term

        final_output = max(min(total_output, self.max_output), -self.max_output)

        return final_output
