import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

# Ask user for number of control points
n = int(input("Enter the number of control points: "))

# Take control points as input
control_points = []
print(f"Enter {n} control points as 'x y' (space-separated):")
for _ in range(n):
    x, y = map(float, input().split())
    control_points.append([x, y])

control_points = np.array(control_points)

# Separate x and y
x = control_points[:, 0]
y = control_points[:, 1]

# Create a B-spline representation
tck, u = interpolate.splprep([x, y], s=0)

# Evaluate B-spline at many points
u_fine = np.linspace(0, 1, 100)
x_fine, y_fine = interpolate.splev(u_fine, tck)

# Plot
plt.plot(x, y, 'ro--', label='Control Points')  # Control points
plt.plot(x_fine, y_fine, 'b-', label='B-spline Curve')  # B-spline curve
plt.legend()
plt.title("B-spline Curve from User Input")
plt.grid(True)
plt.show()
