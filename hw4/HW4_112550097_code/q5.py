import math
from itertools import combinations
# --- Adaptive Trapezoidal Rule for f(x) = 1/x^2 over [0.2, 1] ---
def f_trap(x):
    return 1 / x**2

def trapezoidal(f, a, b, n):
    h = (b - a) / n
    s = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        s += f(a + i * h)
    return s * h

print("\nAdaptive Trapezoidal Rule for f(x) = 1/x^2 over [0.2, 1]:")
a, b = 0.2, 1
n = 1
I_old = trapezoidal(f_trap, a, b, n)
while True:
    n *= 2
    I_new = trapezoidal(f_trap, a, b, n)
    print(f"n={n:4d}, h={(b-a)/n:.5f}, integral={I_new:.6f}, diff={abs(I_new-I_old):.6f}")
    if abs(I_new - I_old) < 0.02:
        break
    I_old = I_new
h_final = (b - a) / n
print(f"\nTerminated at h = {h_final:.5f}, integral = {I_new:.6f}")
