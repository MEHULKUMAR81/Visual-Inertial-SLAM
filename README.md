# Visual-Inertial-SLAM

# Visual-Inertial SLAM using Extended Kalman Filter (EKF)

This repository contains an implementation of a Visual-Inertial SLAM pipeline using an Extended Kalman Filter (EKF) to estimate both the robot's trajectory and the 3D positions of static landmarks from IMU and stereo camera measurements. The project was developed as part of the ECE 276A: Sensing & Estimation in Robotics course at UC San Diego.

## Overview

Visual-Inertial SLAM fuses data from an Inertial Measurement Unit (IMU) and a stereo camera system to simultaneously localize a robot and map its surroundings. In this implementation:
- **IMU Dead Reckoning** integrates linear and angular velocities over time using SE(3) kinematics to obtain an initial trajectory.
- **Landmark Mapping** employs an EKF to update landmark positions based on visual feature measurements.
- **Pose Correction** refines the IMU-based trajectory by incorporating information from landmark observations.


How to Run

1. Install Dependencies
Ensure you have Python 3.8 or higher installed.
Install the required libraries using:
pip install -r requirements.txt

The primary dependencies are:
numpy;scipy;matplotlib;opencv-python;transforms3d



Data Preparation

Place your dataset files (e.g., dataset01.npy and dataset01_imgs.npy) in the data/ folder. These files should include:
IMU measurements (linear and angular velocities, timestamps)
Stereo camera images
Calibration parameters for the camera and IMU



Run the Pipeline

Navigate to the src/ directory and run the main script:
The main pipeline performs the following steps:
Loads IMU and visual data from the data/ folder.
Computes an initial trajectory using IMU dead reckoning via SE(3) integration.
Extracts visual features from the stereo images using ORB.
Performs EKF updates to refine landmark positions and correct the IMU pose.
Visualizes the final trajectory and landmark map in a 2D plot.

