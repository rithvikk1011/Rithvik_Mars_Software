import math

x, y, z = map(float, input("Enter object coords: ").split())
xr, yr, zr = map(float, input("Enter rover position: ").split())
rx, ry, rz = map(float, input("Enter rover's rotation angles: ").split())

rx = math.radians(rx)
ry = math.radians(ry)
rz = math.radians(rz)

# -------- ROTATE ABOUT X --------
x1 = x
y1 = y*math.cos(rx) - z*math.sin(rx)
z1 = y*math.sin(rx) + z*math.cos(rx)

# -------- ROTATE ABOUT Y --------
x2 = x1*math.cos(ry) + z1*math.sin(ry)
y2 = y1
z2 = -x1*math.sin(ry) + z1*math.cos(ry)

# -------- ROTATE ABOUT Z --------
x3 = x2*math.cos(rz) - y2*math.sin(rz)
y3 = x2*math.sin(rz) + y2*math.cos(rz)
z3 = z2

# -------- TRANSLATE --------
x_world = x3 + xr
y_world = y3 + yr
z_world = z3 + zr

# -------- OUTPUT --------
print("Object in World Frame:", (x_world, y_world, z_world))
