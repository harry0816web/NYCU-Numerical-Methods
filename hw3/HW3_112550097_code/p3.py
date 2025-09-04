import numpy as np
import matplotlib.pyplot as plt

# 控制點
control_points = np.array([
    [10, 10],
    [50, 15],
    [75, 60],
    [90, 100],
    [105, 140],
    [150, 200],
    [180, 140],
    [190, 120],
    [160, 100],
    [130, 80]
])
x = control_points[:, 0]
y = control_points[:, 1]

# u from 0 to 1
u = np.linspace(0, 1, 100)

# 定義三段 Bezier 曲線公式
def bezier_curve(P, u):
    return (
        (1 - u) ** 3 * P[0] +
        3 * u * (1 - u) ** 2 * P[1] +
        3 * u**2 * (1 - u) * P[2] +
        u**3 * P[3]
    )

# 第一段 (0,1,2,3)
b1 = bezier_curve(x[0:4], u)
b1_y = bezier_curve(y[0:4], u)

# 第二段 (3,4,5,6)
b2 = bezier_curve(x[3:7], u)
b2_y = bezier_curve(y[3:7], u)

# 第三段 (6,7,8,9)
b3 = bezier_curve(x[6:10], u)
b3_y = bezier_curve(y[6:10], u)

# 畫出來
plt.plot(b1, b1_y, label='Bezier 0-3')
plt.plot(b2, b2_y, label='Bezier 3-6')
plt.plot(b3, b3_y, label='Bezier 6-9')

# 畫控制點
plt.plot(x, y, 'x-', label='Control points', color='black')

plt.legend()
plt.title('Bezier Curves')
plt.grid(True)
plt.show()
