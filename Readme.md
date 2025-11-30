Invisibility Cloak using Python and OpenCV

This project implements a real-time invisibility cloak effect using Python and OpenCV.
The program identifies a specific cloak color and replaces it with the saved background, creating the illusion that the person is invisible.

Overview

The invisibility cloak effect works by capturing the background first, then removing all pixels matching a chosen color (green in this project).
The removed region is filled with the previously captured background, which creates a seamless transparency effect during live video feed.

This project demonstrates concepts in:

Color detection using HSV

Masking and image segmentation

Real-time video processing

Background modeling

Efficient frame blending

Features

Real-time cloak removal

Accurate green mask segmentation

Smooth background restoration

Low-latency processing

Uses an optimized background averaging method

Works on any webcam with no extra hardware

Clean and readable code structure

How It Works

Background Capture
The system captures multiple empty frames and builds a stable background using a weighted average.

Color Detection
The video frame is converted to HSV space.
A specific green range is used to detect the cloak.

Mask Refinement
Morphological filters clean up noise and small errors.

Region Replacement
All green regions are replaced with the captured background.

Final Output
The result appears as if the cloak has disappeared.

Color Range Used (Green)
Lower: [40, 50, 70]
Upper: [90, 255, 255]


These values give high stability and avoid triggering on skin or room objects.

Installation

Install Python 3.8+ and then install the required packages:

pip install opencv-python numpy

Usage

Run the script:

python green_cloak.py


Controls:

Press b: Capture background

Press q: Quit

Folder Structure
Invisibility-Cloak/
│
├── src/
│   └── green_cloak.py
│
├── demo/
│   └── demo.mp4
│
└── README.md

Demo Video

You can view the demo in the demo folder:

demo/demo.mp4

Why Green Cloth?

Green produces the highest contrast against human skin and typical room environments.
It gives cleaner masks, less flicker, and smoother edges compared to red or blue.

Requirements

Python

OpenCV

Webcam

A green-colored cloth

Author

Manisankar
AI and Data Science Engineer