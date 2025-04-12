# 🧠 Micromouse Virtual Simulation - Webots

This folder contains all simulation files required to develop, test, and optimize the **Micromouse Maze Solving Robot** using [Webots](https://cyberbotics.com/), a powerful open-source robotics simulation platform.

---

## 📁 Folder Structure

```
/simulation/
├── controllers/
│   └── micromouse_controller/
│       ├── micromouse_controller.cpp
│       ├── CMakeLists.txt
│       └── Makefile
├── worlds/
│   └── micromouse_maze.wbt
├── protos/
│   └── Micromouse.proto
├── textures/
│   └── maze_texture.jpg
└── README.md

```

---

## 🚗 Robot Description

### Micromouse.proto
Custom robot model definition using Webots' PROTO system:
- ESP32 simulated controller
- 2 Wheels with encoders
- 3 ToF (VL53L0X simulated) sensors: front + 2 angled
- Gyroscope simulated with IMU
- LiPo battery & simple LED indicators

---

## 🌍 World Description

### micromouse_maze.wbt
- Maze dimensions follow IEEE standard (18cm × 18cm cells)
- Start at bottom-left cell (0, 0)
- Goal at center cells (7,7) or (7,8) or (8,7) or (8,8)
- Includes walls, floor textures, and lighting

---

## 🧠 Controller Logic

### micromouse_controller.cpp
Implements:
- Sensor reading abstraction
- Maze wall detection & mapping
- Flood-fill or A* path planning
- PID-based motor control
- Motion profiling for smooth turns & acceleration

You can simulate both **Exploration Run** and **Fast Run**.

---

## 📦 Dependencies

Make sure to have:
- Webots installed
- C/C++ build tools
- Optional: Python interface if you port controller to Python

---

## 🔧 How to Run

1. Open Webots
2. Load the `micromouse_maze.wbt` world
3. Press Play ▶️ to start the simulation
4. Watch your mouse explore and solve the maze in real-time

---

## 📈 Debugging Tools

- Console logs for wall detection and path planning
- Add virtual LEDs or GUI widgets in Webots for real-time feedback
- Use `Supervisor` API for visualizing the optimal path

---

## ✅ TODO

- [ ] Add path visualizer
- [ ] Improve motion profiling
- [ ] Create complex mazes for stress-testing

---

## 📚 References

- [Micromouse Algorithms – Wikipedia](https://en.wikipedia.org/wiki/Micromouse)
- [Webots Docs](https://cyberbotics.com/doc/guide/index)
- [Flood Fill Algorithm](https://www.jianshu.com/p/07e4e0f26e90)

---

## 🧑‍💻 Author & Maintainers

Developed by: Bots  
University: `University of Peradeniya`  
Year: 2025 April

---
