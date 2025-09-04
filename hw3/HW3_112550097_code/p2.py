import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 6 * (x + 1)**3 - 3 * (x + 1)**2

# Define the cubic spline segments
def g0(x):
    return 6 * (x + 1)**3 - 3 * (x + 1)**2

def g1(x):
    return -10 * (x + 0.5)**3 + 6 * (x + 0.5)**2 + 1.5 * (x + 0.5)

def g2(x):
    return 10 * x**3 - 9 * x**2 + 1

def g3(x):
    return -6 * (x - 0.5)**3 + 6 * (x - 0.5)**2 - 1.5 * (x - 0.5)

# Define the x ranges for each segment
x0 = np.linspace(-1, -0.5, 100)
x1 = np.linspace(-0.5, 0, 100)
x2 = np.linspace(0, 0.5, 100)
x3 = np.linspace(0.5, 1, 100)

# Plot the cubic spline segments
plt.figure()
plt.plot(x0, g0(x0), label='g0(x)')
plt.plot(x1, g1(x1), label='g1(x)')
plt.plot(x2, g2(x2), label='g2(x)')
plt.plot(x3, g3(x3), label='g3(x)')

# Evaluate g1 at the boundaries
g1_minus_0_5 = g1(-0.5)
g1_0 = g1(0)
print(f"g1(-0.5) = {g1_minus_0_5}")
print(f"g1(0) = {g1_0}")

# Define the piecewise linear functions
def p0(x):
    return 0 * x

def p1(x):
    return 1 + 2 * x

def p2(x):
    return 1 - 2 * x

def p3(x):
    return 0 * x
x = np.array([-1, -0.5, 0, 0.5, 1])
y = np.array([0, 0, 1, 0, 0])

# Plot the piecewise linear functions
plt.plot(x0, p0(x0), label='p0(x)')
plt.plot(x1, p1(x1), label='p1(x)')
plt.plot(x2, p2(x2), label='p2(x)')
plt.plot(x3, p3(x3), label='p3(x)')
plt.plot(x, y, 'black', marker='o', linestyle='-', label='f(x)')

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
# plt.title('Piecewise Cubic and Linear Functions')
# plt.legend()
plt.grid(True)
plt.show()