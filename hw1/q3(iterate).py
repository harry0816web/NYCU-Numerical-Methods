from math import sqrt
def g(x):
    return sqrt(4/x)

tol = 1e-5
def iterate(x0, tol):
    x1 = g(x0)
    while abs(x1 - x0) > tol:
        x0 = x1
        x1 = g(x0)
    return x1

print(iterate(1.0, tol)) # 1.5873982537565454