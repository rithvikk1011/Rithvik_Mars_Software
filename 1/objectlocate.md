This program converts an object’s position from the rover’s coordinate system to the world coordinate system.

Input:
Object coordinates → (x, y, z)
Rover position → (xr, yr, zr)
Rover rotation → (rx, ry, rz) in degrees

Steps:
1. Convert angles
Rotation angles are converted from degrees to radians because Python’s sin and cos use radians.
2. Apply rotations

Rotate about X, Y, Z axis. In each rotation that specific coordinate remains same. For exmaple: For rotation about X axis, X coordinate is the sasme
The formulas used are the basic formulas used to rotate the frame of reference
These rotations adjust the object based on the rover’s orientation.

3. Apply translation
After rotation, we shift the object using the rover’s position: Final position = rotated position + rover position
