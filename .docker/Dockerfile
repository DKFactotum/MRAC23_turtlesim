ARG ROSDISTRO=noetic

FROM ros:$ROSDISTRO-robot as base

ARG ROSDISTRO

# Set environment variables
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive
ENV TERM xterm-256color

RUN apt-get update && apt-get install --no-install-recommends -y \
    wget \
    ssh \
    git \
    curl \
    python3-pip \
    python3-flake8 \
    build-essential \
    cmake \
    terminator \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install -U --no-cache-dir\
    catkin_tools \
    argcomplete \
    flake8-blind-except \
    flake8-builtins \
    flake8-class-newline \
    flake8-comprehensions \
    flake8-deprecated \
    flake8-return \
    flake8-length \
    flake8-todo \
    flake8-quotes \
    autopep8

RUN apt-get update && apt-get install --no-install-recommends -y \
    pkg-config \
    python3-catkin-tools \
    python3-rosdep \
    python3-rosinstall-generator \
    python3-vcstool \
    ros-$ROSDISTRO-rqt \
    ros-$ROSDISTRO-rqt-action \
    ros-$ROSDISTRO-rqt-plot \
    ros-$ROSDISTRO-rqt-console \
    ros-$ROSDISTRO-rqt-service-caller \
    ros-$ROSDISTRO-rqt-graph \
    ros-$ROSDISTRO-rqt-topic \
    ros-$ROSDISTRO-rqt-top \
    ros-$ROSDISTRO-rqt-reconfigure \
    ros-$ROSDISTRO-rqt-tf-tree \
    ros-$ROSDISTRO-ros-tutorials \
    ros-$ROS_DISTRO-rosbridge-suite \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN ["/bin/bash", "-c", "rm -rf /var/lib/apt/lists/*"]

# Create workspace
RUN mkdir -p dev_ws/src
WORKDIR /dev_ws/src
# Copy local pkg's from host to container
COPY . /dev_ws/src/


# Bash final stage
# ----------------------------------------
FROM base as bash

ARG ROSDISTRO

# # Build catkin workspace
# WORKDIR /dev_ws
# RUN ["/bin/bash", "-c", "source /opt/ros/$ROSDISTRO/setup.bash &&\
#     catkin config --cmake-args -DCMAKE_BUILD_TYPE=Release &&\
#     catkin build \
#     "]

# Copy and make setup script executable
COPY .docker/setup.bash /dev_ws/setup.bash
RUN ["/bin/bash", "-c", " chmod 777 /dev_ws/setup.bash"]

# Copy and make entrypoint script executable
RUN ["/bin/bash", "-c", "cp /dev_ws/src/.docker/entrypoint.sh / && chmod 777 /entrypoint.sh"]
ENTRYPOINT [ "/entrypoint.sh" ]

# Start bash shell
CMD ["bash"]


# Zsh final stage
# ----------------------------------------
FROM base as zsh

# install zsh and remove apt cache
RUN apt-get update && apt-get install -y \
    zsh \
    && rm -rf /var/lib/apt/lists/*

# Set shell to zsh
SHELL ["zsh", "chsh -s ~/.zshrc" ]

# # Build catkin workspace
# WORKDIR /dev_ws
# RUN ["/bin/bash", "-c", "source /opt/ros/$ROSDISTRO/setup.bash &&\
#     catkin config --cmake-args -DCMAKE_BUILD_TYPE=Release &&\
#     catkin build \
#     "]

# Copy and make setup script executable
COPY .docker/setup.zsh /dev_ws/setup.zsh
RUN ["/bin/bash", "-c", " chmod 777 /dev_ws/setup.zsh"]

# Copy and make entrypoint script executable
COPY .docker/entrypoint_zsh.sh /entrypoint_zsh.sh
RUN ["/bin/bash", "-c", "chmod 777 /entrypoint_zsh.sh"]
ENTRYPOINT ["zsh", "/entrypoint_zsh.sh" ]

# start ZSH shell
CMD ["zsh"]