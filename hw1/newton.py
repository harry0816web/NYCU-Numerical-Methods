import math
def f(x):
    return x**2 + math.sin(x) - math.exp(x)/4 - 1
def fprime(x):
    return 2 * x + math.cos(x) - math.exp(x)/4

tol = 1e-5
def newton(x0, tol):
    x1 = x0 - f(x0) / fprime(x0)
    while abs(f(x1)) > tol:
        x1 = x1 - f(x1) / fprime(x1)
    return x1

print(newton(-2, tol))
print(newton(0, tol))


# -1.4318086009771325
# 0.9119186162195468