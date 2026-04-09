This program creates a map of the Mars arena for Rover Brick.
It reads obstacle positions from a file called "sample.txt" and marks them on an n x n grid.
Safe spots = 1, Obstacles = 0.

Each line in sample.txt has 4 numbers: N E S W
N = distance north from the origin (0,0)
E = distance east from the origin
S = distance south from the origin
W = distance west from the origin

Example:
2 3 0 3
Means:
- Block 2 cells north
- Block 3 cells east
- Block 0 cells south
- Block 3 cells west


- Arena is a 2D list (matrix) of size 11x11
- All cells start as 1 (safe)
- Obstacles from the file are set to 0
