# Visual-Inertial-SLAM

# Visual-Inertial SLAM using Extended Kalman Filter (EKF)

This repository contains an implementation of a Visual-Inertial SLAM pipeline using an Extended Kalman Filter (EKF) to estimate both the robot's trajectory and the 3D positions of static landmarks from IMU and stereo camera measurements. The project was developed as part of the ECE 276A: Sensing & Estimation in Robotics course at UC San Diego.

## Overview

Visual-Inertial SLAM fuses data from an Inertial Measurement Unit (IMU) and a stereo camera system to simultaneously localize a robot and map its surroundings. In this implementation:
- **IMU Dead Reckoning** integrates linear and angular velocities over time using SE(3) kinematics to obtain an initial trajectory.
- **Landmark Mapping** employs an EKF to update landmark positions based on visual feature measurements.
- **Pose Correction** refines the IMU-based trajectory by incorporating information from landmark observations.
