from src.ball_tracker.ball_tracker.geometry import convert_camera_pixels_to_turtlesime_corrdinates


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
