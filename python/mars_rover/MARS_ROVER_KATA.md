# 🤖 The Kata: Mars Rover (Codurance Version)

**Source**: [https://www.codurance.com/katas/mars-rover](https://www.codurance.com/katas/mars-rover)

## Your Task
You’re part of the team that explores Mars by sending remotely controlled vehicles to the surface of the planet. Develop an API that translates the commands sent from earth to instructions that are understood by the rover.

## Requirements

### 1. Initialization
The rover is given an initial starting point (x, y) and the direction (N, S, E, W) it is facing.
-   Example: `x=0, y=0, direction=N`

### 2. Commands
The rover receives a character array of commands.
-   `M`: Move forward one grid point.
-   `L`: Turn Left 90 degrees.
-   `R`: Turn Right 90 degrees.

### 3. Wrapping
The rover wraps around if it reaches the end of the grid.
-   The grid may be defined as 10x10 (or any size).
-   Moving North from (0, 9) goes to (0, 0).

### 4. Output
The rover should return its final position and direction.
-   Format: `X:Y:Direction`
-   Example: `2:3:E`

### 5. Obstacles
The grid may have obstacles. If a given sequence of commands encounters an obstacle, the rover moves up to the last possible point, aborts the sequence and reports the obstacle.
-   Format: `O:X:Y:Direction` (prefixed with `O:`)
-   Example: `O:1:1:N` (Obstacle hit, stopped at 1:1 facing North)