import math

# Input for object coordinates
x, y, z = map(float, input("Enter object coords: ").split())

# Rover's position in world frame
xr, yr, zr = map(float, input("Enter rover position: ").split())

# Rover's rotation angles (in degrees)
rx, ry, rz = map(float, input("Enter rover's rotation angles: ").split())

# Convert degrees to radians
rx = math.radians(rx)
ry = math.radians(ry)
rz = math.radians(rz)


# Rotate the object around X-axis: X stays same, Y and Z change
x1 = x
y1 = y*math.cos(rx) - z*math.sin(rx)
z1 = y*math.sin(rx) + z*math.cos(rx)

# Rotate around Y-axis: Y stays same, X and Z change
x2 = x1*math.cos(ry) + z1*math.sin(ry)
y2 = y1
z2 = -x1*math.sin(ry) + z1*math.cos(ry)

# Rotate around Z-axis: Z stays same, X and Y change
x3 = x2*math.cos(rz) - y2*math.sin(rz)
y3 = x2*math.sin(rz) + y2*math.cos(rz)
z3 = z2


# After rotation, shift the object by rover's position
# This converts from rover frame → world frame
x_world = x3 + xr
y_world = y3 + yr
z_world = z3 + zr

print("Object in World Frame:", (x_world, y_world, z_world))
