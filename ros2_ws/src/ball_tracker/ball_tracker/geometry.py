import math


def convert_camera_pixels_to_turtlesime_corrdinates(pixel_x, pixel_y):
    sim_x = (pixel_x / 500.0) * 11.0
    sim_y = ((500.0 - pixel_y) / 500.0) * 11.0
    return sim_x, sim_y


def calculate_distance(current_x, current_y, target_x, target_y):
    return math.sqrt((target_x - current_x) ** 2 + (target_y - current_y) ** 2)


def calculate_angle_error(current_theta, current_x, current_y, target_x, target_y):
    target_angle = math.atan2(target_y - current_y, target_x - current_x)
    error = target_angle - current_theta
    return math.atan2(math.sin(error), math.cos(error))
