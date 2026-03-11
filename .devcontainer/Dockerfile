FROM osrf/ros:humble-desktop

RUN apt-get update && apt-get install -y \
    python3-pip \
    ros-humble-turtlesim \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

COPY requirements.txt .
RUN pip install --upgrade pip setuptools packaging
RUN pip install -r requirements.txt

COPY . .

SHELL ["/bin/bash", "-c"]

WORKDIR /workspace/ros2_ws
RUN source /opt/ros/humble/setup.bash && colcon build

RUN chmod +x /workspace/run_tracker.sh

ENTRYPOINT ["/bin/bash", "/workspace/run_tracker.sh"]
