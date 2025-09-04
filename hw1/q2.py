import math
def f(x):
    return(x-2)**3 * (x-4)**2
def fprime(x):
    return 3*((x-2)**2) * ((x-4)**2) + 2*((x-2)**3) * (x-4)

tol = 1e-5
def newton(x0, tol):
    x1 = x0 - f(x0) / fprime(x0)
    while abs(f(x1)) > tol:
        x1 = x1 - f(x1) / fprime(x1)
    return x1

print('root:', newton(3.0, tol))


# -1.4318086009771325
# 0.9119186162195468