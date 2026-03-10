def pixels_to_turtlesim(pixel_x, pixel_y):
    sim_x = (pixel_x / 500.0) * 11.0
    sim_y = ((500.0 - pixel_y) / 500.0) * 11.0
    return sim_x, sim_y
