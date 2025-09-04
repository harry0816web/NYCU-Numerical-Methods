import numpy as np
import math

# 定義目標函數
def f(x):
    return x + math.sin(x) / 3

# 建立差商表
def divided_difference(xs, ys):
    n = len(xs)
    table = np.zeros((n, n))
    table[:, 0] = ys
    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = (table[i + 1][j - 1] - table[i][j - 1]) / (xs[i + j] - xs[i])
    return table[0]

# 計算 Newton 插值多項式的導數
def derivative_of_newton_poly(xs, coeffs, x_val):
    n = len(coeffs)
    derivative = 0
    for k in range(1, n):
        sum_terms = 0
        for j in range(k):
            prod = 1
            for i in range(k):
                if i != j:
                    prod *= (x_val - xs[i])
            sum_terms += prod
        derivative += coeffs[k] * sum_terms
    return derivative

# 選取最佳起始點
# 原則：選取最靠近目標點的連續資料點，確保插值多項式在目標點附近誤差最小。
# 步驟：計算每個資料點與目標點的距離，排序後取最近的 degree+1 個點，並依 x 值大小排序。
def select_best_points(xs, target, degree):
    distances = [abs(x - target) for x in xs]
    sorted_indices = np.argsort(distances)
    best_indices = sorted(sorted_indices[:degree + 1])
    return [xs[i] for i in best_indices]

def forward_difference_table(xs, ys, max_order=4):
    n = len(xs)
    table = np.zeros((n, max_order+2))
    table[:, 0] = xs
    table[:, 1] = ys
    for j in range(2, max_order+2):
        for i in range(n - (j-1)):
            table[i][j] = table[i+1][j-1] - table[i][j-1]
    # Print the table
    header = ["i", "xi", "f(xi)"] + [f"Δ^{k}f" for k in range(1, max_order+1)]
    print("\t".join(header))
    for i in range(n):
        row = [f"{i}", f"{table[i][0]:.2f}", f"{table[i][1]:.6f}" if abs(table[i][1]) > 1e-12 else ""]
        for j in range(2, max_order+2):
            val = table[i][j]
            if i <= n - (j-1):
                row.append(f"{val:.6f}" if abs(val) > 1e-12 else "")
            else:
                row.append("")
        print("\t".join(row))
    return table

# 資料點
xs_all = [0.3, 0.5, 0.7, 0.9, 1.1, 1.3, 1.5]
ys_all = [f(x) for x in xs_all]

# 建立並輸出前向差分表（到 Δ^4）
print("Forward Difference Table (up to Δ^4):")
forward_difference_table(xs_all, ys_all, max_order=4)

# (a) f'(0.72) 使用 3 次多項式 (4 點)
target_a = 0.72
points_a = [0.7, 0.9, 1.1, 1.3]
ys_a = [f(x) for x in points_a]
coeffs_a = divided_difference(points_a, ys_a)
result_a = derivative_of_newton_poly(points_a, coeffs_a, target_a)

# (b) f'(1.33) 使用 2 次多項式 (3 點)
target_b = 1.33
points_b = [1.1, 1.3, 1.5]
ys_b = [f(x) for x in points_b]
coeffs_b = divided_difference(points_b, ys_b)
result_b = derivative_of_newton_poly(points_b, coeffs_b, target_b)

# (c) f'(0.50) 使用 4 次多項式 (5 點)
target_c = 0.50
points_c = select_best_points(xs_all, target_c, 4)
ys_c = [f(x) for x in points_c]
coeffs_c = divided_difference(points_c, ys_c)
result_c = derivative_of_newton_poly(points_c, coeffs_c, target_c)

# 輸出結果
print("(a) f'(0.72) 估計值：", result_a, "，使用點：", points_a)
print("(b) f'(1.33) 估計值：", result_b, "，使用點：", points_b)
print("(c) f'(0.50) 估計值：", result_c, "，使用點：", points_c)
