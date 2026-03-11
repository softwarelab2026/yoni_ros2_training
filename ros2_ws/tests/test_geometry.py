import math

import pytest
from src.ball_tracker.ball_tracker.geometry import (
    calculate_angle_error,
    calculate_distance,
    convert_camera_pixels_to_turtlesime_corrdinates,
)


def test_pixels_to_turtlesim_top_left():
    sim_x, sim_y = convert_camera_pixels_to_turtlesime_corrdinates(0, 0)
    assert sim_x == 0.0
    assert sim_y == 11.0


def test_pixels_to_turtlesim_bottom_right():
    sim_x, sim_y = convert_camera_pixels_to_turtlesime_corrdinates(500, 500)
    assert sim_x == 11.0
    assert sim_y == 0.0


def test_pixels_to_turtlesim_center():
    sim_x, sim_y = convert_camera_pixels_to_turtlesime_corrdinates(250, 250)
    assert sim_x == 5.5
    assert sim_y == 5.5


def test_pixels_to_turtlesim_asymmetric():
    sim_x, sim_y = convert_camera_pixels_to_turtlesime_corrdinates(0, 250)
    assert sim_x == 0.0
    assert sim_y == 5.5


def test_calculate_distance():
    assert calculate_distance(0.0, 0.0, 3.0, 4.0) == pytest.approx(5.0)
    assert calculate_distance(5.0, 5.0, 8.0, 9.0) == pytest.approx(5.0)


def test_angle_error_cases():
    assert calculate_angle_error(0.0, 0.0, 0.0, 0.0, 0.1) > 0
    assert calculate_angle_error(0.0, 0.0, 0.0, 0.0, -0.1) < 0
    assert calculate_angle_error(math.pi / 2, 0.0, 0.0, 0.1, 1.0) < 0
    assert calculate_angle_error(math.pi / 2, 0.0, 0.0, -0.1, 1.0) > 0
    assert calculate_angle_error(-math.pi / 2, 0.0, 0.0, 0.1, -1.0) > 0
    assert calculate_angle_error(-math.pi / 2, 0.0, 0.0, -0.1, -1.0) < 0
    assert calculate_angle_error(math.pi, 0.0, 0.0, -1.0, 0.1) < 0
    assert calculate_angle_error(math.pi, 0.0, 0.0, -1.0, -0.1) > 0


def test_calculate_angle_error_shortest_path():
    current_theta = math.pi - 0.1
    error = calculate_angle_error(current_theta, 0.0, 0.0, 1.0, -1.0)
    assert error > 0
    assert math.isclose(error, 2.456, rel_tol=1e-3)
    error_wrap = calculate_angle_error(math.pi - 0.1, 0.0, 0.0, -1.0, -0.1)
    assert abs(error_wrap) < 1.0
    assert error_wrap > 0
