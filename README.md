# Phys 499 - Assignment II (Fall 2024)

## Overview

This repository contains the solutions for **Phys 499 Assignment II**, due on October 16th, 2024. The tasks involve simulations related to the **Monty Hall Problem** and the **Sierpinski Triangle**, as described below.

## Contents

- **assignment_II_Fall_2024.pdf**: The original assignment document.
- **ThreeDoorsSimulationNoDoorOpened.py**: Python script for simulating the Monty Hall problem.
- **drawpolygon.py**: Helper functions for drawing polygons, used in the Sierpinski Triangle program.
- **output_text_file.txt**: Results from running the Monty Hall simulation.
- **sierpinski.py**: Program to draw the Sierpinski Triangle using recursion.

## Assignment Description

### Q1: Monty Hall Problem

The Monty Hall problem is a famous probability puzzle based on a game show scenario:

1. There are three doors, behind one of which is a car, and behind the others are goats.
2. The player picks a door.
3. The host, knowing what's behind each door, opens one of the other two doors to reveal a goat.
4. The player is then given the option to switch to the remaining unopened door.

**Task**: Simulate the Monty Hall problem in Python, proving that switching doors results in a higher chance of winning the car (approximately 2/3).

**Simulation Requirements**:
- Randomly place the car behind one of the doors.
- Allow the player to choose a door.
- Simulate the host revealing a goat behind one of the other doors.
- Track the success rate for the player who switches doors over multiple iterations (e.g., 10,000, 100,000, and 1,000,000 trials).

### Q2: Sierpinski Triangle

The Sierpinski triangle is a fractal pattern:

1. It starts with an equilateral triangle.
2. The triangle is recursively subdivided into smaller equilateral triangles.

**Task**: Write a Python program using a recursive function to plot the Sierpinski triangle. The program should:
- Take an integer input `N` representing the recursion depth.
- Use Turtle graphics for visualization.
- Draw the initial triangle and recursively generate smaller triangles.
