import math

# 資料點
data = [0.15, 0.21, 0.23, 0.27, 0.32, 0.35]

def f(x):
    return 1 + math.log10(x)

def f_prime_true(x):
    return 1 / (x * math.log(10))

# 1. 列出完整差分表
n = len(data)
table = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    table[i][0] = f(data[i])
for j in range(1, n):
    for i in range(n-j):
        table[i][j] = (table[i+1][j-1] - table[i][j-1]) / (data[i+j] - data[i])

# 輸出差分表
header = ["i", "xi", "f(xi)"] + [f"{k}th diff" for k in range(1, n)]
print("\t".join(header))
for i in range(n):
    row = [f"{i}", f"{data[i]:.5f}", f"{table[i][0]:.6f}"]
    for j in range(1, n-i):
        row.append(f"{table[i][j]:.6f}")
    print("\t".join(row))

# 2. 只用連續三點組合
x_target = 0.268
true_val = f_prime_true(x_target)

best_error = float('inf')
best_points = None
best_interp = None

print("\n連續三點組合、插值導數、真值、誤差：")
for i in range(n-2):
    xs = data[i:i+3]
    ys = [f(x) for x in xs]
    # 差商表
    t = [[0 for _ in range(3)] for _ in range(3)]
    for k in range(3):
        t[k][0] = ys[k]
    for j in range(1, 3):
        for k in range(3-j):
            t[k][j] = (t[k+1][j-1] - t[k][j-1]) / (xs[k+j] - xs[k])
    # Newton 二次多項式的導數在 x_target
    interp_prime = t[0][1] + t[0][2]*((x_target-xs[0]) + (x_target-xs[1]))
    error = abs(interp_prime - true_val)
    print(f"{xs}  f'={interp_prime:.6f}  真值={true_val:.6f}  誤差={error:.2e}")
    if error < best_error:
        best_error = error
        best_points = xs
        best_interp = interp_prime

print(f"\n最佳連續三點組合: {best_points}")
print(f"對應插值導數: {best_interp:.6f}")
print(f"真值: {true_val:.6f}")
print(f"最小誤差: {best_error:.2e}")
