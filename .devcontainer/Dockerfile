FROM osrf/ros:humble-desktop

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    wget \
    curl \
    python3-pip \
    software-properties-common \
    ros-dev-tools \
    ros-humble-turtlesim

RUN pip install -U \
    setuptools \
    colcon-common-extensions

RUN echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc

CMD ["bash"]