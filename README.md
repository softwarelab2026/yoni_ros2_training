# yoni's ros2 ball tracker

## how it works
* a virtual camera node generates a moving red ball and publishes frames to `/camera/image_raw`.
* the tracker node processes these frames using color segmentation (`cv2.inRange`) and image moments to find the ball's center.
* a custom controller calculates the distance and angle to the ball and publishes velocity commands to `/turtle1/cmd_vel` using a pid logic i wrote.

## how to run it
i set this up to be easy to run either for development or just to test the final code.

### option 1: production (docker compose)
if you just want to run the final project to see it work:
1. open a terminal and allow gui connections:
   ```bash
   xhost +
   ```

2. run docker compose:
    ```bash
    docker compose up
    ```
this will build the image and launch the turtlesim window + the camera feed all at once.

### option 2: development (vscode tasks)
if you want to look at the code or edit it, i set up vs code tasks so you don't have to type out long ros2 commands manually.

1. open the project folder in vscode and click "reopen in container" (this uses the .devcontainer setup).
2. go to the top menu: Terminal -> Run Task...
3. pick the task `"Clean, Build and Launch System"`.

the task will do all the dirty work for you: it cleans the old build, runs colcon build --symlink-install, sources the workspaces, and executes the correct ros2 launch file. no manual node running needed!
