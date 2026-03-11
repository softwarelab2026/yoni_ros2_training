# yoni's ball tracker project - summary

## what is this?
so, for this assignment, i had to make the turtlesim robot follow a moving red ball. the cool part is that it's a "closed-loop" system, meaning the robot "sees" where the ball is and adjusts its movement in real-time to catch up. i used ros2 humble, some opencv for the vision part, and a pid controller for the movement logic.

## how i built it
i split it into 4 nodes:
1. **virtual_camera**: this one just creates a 500x500 window and makes a red ball bounce around.
2. **ball_tracker**: the "eyes" of the project. it gets the camera frames and finds the ball.
3. **turtle_controller**: the "brain". it decides how fast the turtle should turn or run based on the ball's position.
4. **turtlesim_node**: the classic ros2 simulator we all know.

## the vision part (opencv)
to find the ball, i used two main steps:
* **masking**: i used `cv2.inRange` to tell the computer: "hey, only look at these specific red pixels and ignore everything else".
* **moments**: once i had the red pixels, i used `cv2.moments` to calculate the center of the ball. it's basically a math trick that finds the "middle" of all the red dots it found.

## the movement (pid control)
for the actual driving, i wrote a **pid controller**.
* **heading**: the turtle checks its current angle vs where the ball is (using `atan2`) and turns to face it.
* **speed**: i made it so the turtle moves faster when the ball is far away and slows down as it gets closer so it doesn't just crash into it.
* i mostly tuned the **P (proportional)** gain to keep it simple and stable, so it follows the ball smoothly without wobbling too much.

## challenges i had
the trickiest part was definitely the coordinates. the camera uses pixels (0 to 500) and starts from the top-left, but turtlesim uses a 0 to 11 scale and starts from the bottom-left. i had to write a small helper function in `geometry.py` to map these values and flip the Y-axis so the turtle doesn't go the wrong way..

## bottom line
the system works good. the turtle is actually pretty good at tracking the ball, even when it bounces fast.
