import numpy as np

# 定義積分函數
def f(x, y):
    return np.exp(x) * np.sin(2 * y)

# 三點高斯積分的節點與權重
nodes = np.array([-0.77459667,0,0.77459667])
weights = np.array([0.55555555,0.88888889,0.55555555])

# 區間設定與步長 h
x_start, x_end = -0.2, 1.4
y_start, y_end = 0.4, 2.6
h = 0.1

# 累加積分值
integral = 0.0
x_panels = np.arange(x_start, x_end, h)
y_panels = np.arange(y_start, y_end, h)

for i in range(len(x_panels)):
    for j in range(len(y_panels)):
        x_a, x_b = x_panels[i], x_panels[i] + h
        y_a, y_b = y_panels[j], y_panels[j] + h

        for xi in range(3):
            for yi in range(3):
                # 範圍映射到 [-1,1] -> [a,b]
                x = 0.5 * (x_b - x_a) * nodes[xi] + 0.5 * (x_b + x_a)
                y = 0.5 * (y_b - y_a) * nodes[yi] + 0.5 * (y_b + y_a)
                w = weights[xi] * weights[yi]
                integral += w * f(x, y) * 0.25 * (x_b - x_a) * (y_b - y_a)

print(integral)
