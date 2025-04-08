# 🏁 Maze Solving Robot 🤖

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![ROS Noetic](https://img.shields.io/badge/ROS-Noetic-brightgreen.svg)](https://www.ros.org/)

An autonomous robot that navigates complex mazes using sensor fusion and pathfinding algorithms. Perfect for robotics competitions and STEM education!

## 🌟 Features
- 🧩 Multiple solving algorithms (Wall Follower, Flood Fill, Tremaux)
- 🖥️ ROS/Gazebo simulation support
- 📊 Real-time maze visualization
- 🔧 Modular architecture for easy customization
- 📶 Support for various sensor configurations

## 📦 Hardware Requirements
| Component | Specification |
|-----------|--------------|
| Microcontroller | Arduino Mega/Raspberry Pi 4 |
| Sensors | Ultrasonic x3 / LIDAR (RPLIDAR A1) |
| Motors | 6V DC Geared Motors (100 RPM) |
| Chassis | 2WD/4WD Robot Base |

## 🛠️ Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/maze-solving-robot.git
cd maze-solving-robot

# Install dependencies
pip install -r requirements.txt

# For ROS simulation (optional)
catkin_make
source devel/setup.bash
