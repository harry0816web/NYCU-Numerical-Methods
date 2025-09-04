import numpy as np

# 資料
x = np.array([1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8])
y = np.array([1.543, 1.669, 1.811, 1.971, 2.151, 2.352, 2.577, 2.828, 3.107])
h = 0.1

# Simpson's 1/3 rule
def simpson_13(y0, y1, y2, h):
    return h/3 * (y0 + 4*y1 + y2)

# Simpson's 3/8 rule
def simpson_38(y0, y1, y2, y3, h):
    return 3*h/8 * (y0 + 3*y1 + 3*y2 + y3)

# 1. 全部用 1/3 rule
I_13_all = (
    simpson_13(y[0], y[1], y[2], h) +
    simpson_13(y[2], y[3], y[4], h) +
    simpson_13(y[4], y[5], y[6], h) +
    simpson_13(y[6], y[7], y[8], h)
)
print(f"全部用 1/3 rule (正確答案): {I_13_all:.6f}")

# 2. 2 組 3/8 + 1 組 1/3，連續分法
results = []
# (a) 3/8 on [0:3], 3/8 on [3:6], 1/3 on [6:8]
I_a = simpson_38(y[0], y[1], y[2], y[3], h) + simpson_38(y[3], y[4], y[5], y[6], h) + simpson_13(y[6], y[7], y[8], h)
results.append(("3/8[0:3],3/8[3:6],1/3[6:8]", I_a, abs(I_a - I_13_all)))

# (b) 3/8 on [0:3], 1/3 on [3:5], 3/8 on [5:8]
I_b = simpson_38(y[0], y[1], y[2], y[3], h) + simpson_13(y[3], y[4], y[5], h) + simpson_38(y[5], y[6], y[7], y[8], h)
results.append(("3/8[0:3],1/3[3:5],3/8[5:8]", I_b, abs(I_b - I_13_all)))

# (c) 1/3 on [0:2], 3/8 on [2:5], 3/8 on [5:8]
I_c = simpson_13(y[0], y[1], y[2], h) + simpson_38(y[2], y[3], y[4], y[5], h) + simpson_38(y[5], y[6], y[7], y[8], h)
results.append(("1/3[0:2],3/8[2:5],3/8[5:8]", I_c, abs(I_c - I_13_all)))

print("\n2 組 3/8 + 1 組 1/3 (連續分法) 與正確答案的誤差：")
for label, val, err in results:
    print(f"{label}: 積分值={val:.6f}, 誤差={err:.2e}")

best = min(results, key=lambda t: t[2])
print(f"\n最佳分法: {best[0]}, 誤差={best[2]:.2e}")