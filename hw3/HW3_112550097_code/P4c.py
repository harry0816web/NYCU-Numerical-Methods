import numpy as np
import matplotlib.pyplot as plt

# 控制點
control_points = np.array([
    [10, 10],
    [10, 10],
    [10, 10],
    [50, 15],
    [75, 60],
    [90, 100],
    [105, 140],
    [150, 200],
    [180, 140],
    [190, 120],
    [160, 100],
    [130, 80],
    [130, 80],
    [130, 80]
])

x = control_points[:, 0]
y = control_points[:, 1]

# u 在 [0,1] 之間
u = np.linspace(0, 1, 100)
u2 = np.linspace(1, 2, 100)
u3 = np.linspace(2, 3, 100)

# 定義 uniform cubic B-spline basis functions
def B_spline_basis(u):
    b0 = (1 - u)**3 / 6
    b1 = (3*u**3 - 6*u**2 + 4) / 6
    b2 = (-3*u**3 + 3*u**2 + 3*u + 1) / 6
    b3 = u**3 / 6
    return b0, b1, b2, b3

# 畫每一小段
# for i in range(2,9):  # 0~6 (因為總共有10個點，要畫10-3=7段)
#     b0, b1, b2, b3 = B_spline_basis(u)
#     g_x = b0 * x[i-2] + b1 * x[i-1] + b2 * x[i] + b3 * x[i+1]
#     g_y = b0 * y[i-2] + b1 * y[i-1] + b2 * y[i] + b3 * y[i+1]
#     plt.plot(g_x, g_y)

# draw with diffrent u (p0-p3 with u in [0,1]), (p3-p6 with u in [1,2]), (p6-p9 with u in [2,3])

# 畫控制點
plt.plot(x, y, 'x-', label='Control points', color='black')

for i in range(2, 12): 
    if i <= 3:
        b0, b1, b2, b3 = B_spline_basis(u)
        g_x = b0 * x[i-2] + b1 * x[i-1] + b2 * x[i] + b3 * x[i+1]
        g_y = b0 * y[i-2] + b1 * y[i-1] + b2 * y[i] + b3 * y[i+1]
    elif i <= 6:
        b0, b1, b2, b3 = B_spline_basis(u2 - 1)
        g_x = b0 * x[i-2] + b1 * x[i-1] + b2 * x[i] + b3 * x[i+1]
        g_y = b0 * y[i-2] + b1 * y[i-1] + b2 * y[i] + b3 * y[i+1]
    else:
        b0, b1, b2, b3 = B_spline_basis(u3 - 2)
        g_x = b0 * x[i-2] + b1 * x[i-1] + b2 * x[i] + b3 * x[i+1]
        g_y = b0 * y[i-2] + b1 * y[i-1] + b2 * y[i] + b3 * y[i+1]

    plt.plot(g_x, g_y, color='blue')



plt.title('B-spline Curves')
plt.grid(True)
plt.legend()
plt.show()
