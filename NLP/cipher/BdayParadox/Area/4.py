import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

# Fixed control points (example similar to your sketch)
control_points = np.array([
    [5, 2],
    [15, 9],
    [30, 4],
    [50, 5],
    [70, 2]
])

# Separate x and y
x = control_points[:, 0]
y = control_points[:, 1]

# Degree of B-spline (cubic = degree 3)
degree = 3

# Create B-spline representation
tck, u = interpolate.splprep([x, y], s=0, k=degree)

# Evaluate B-spline at many points
u_fine = np.linspace(0, 1, 400)
x_fine, y_fine = interpolate.splev(u_fine, tck)

# Plot
plt.figure(figsize=(8, 5))
plt.plot(x, y, 'ro--', label='Control Polygon', linestyle='dashed')  # Dashed control polygon
plt.plot(x_fine, y_fine, 'b-', label='B-spline Curve (degree=3)')    # Smooth B-spline curve
plt.scatter(x, y, color='red')  # Points P1, P2, etc.

# Label the control points
for idx, (xi, yi) in enumerate(zip(x, y)):
    plt.text(xi + 1, yi + 0.5, f'P{idx+1}', fontsize=9)

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Cubic B-spline Curve with Control Polygon')
plt.legend()
plt.grid(True)
plt.show()
