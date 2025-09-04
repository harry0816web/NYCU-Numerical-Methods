import math

print('result (round to 5 decimal places)')
print('')

def f(x):
    return x**2 + math.sin(x) - math.exp(x)/4 - 1

tol = 1e-5
def bisection(a, b, tol):
    m = (a + b) / 2
    while(abs(f(m)) > tol):
        if(f(m) == 0):  # 剛好是解
            return m

        if f(a) * f(m) < 0:
            b = m
        else:
            a = m
        m = (a + b) / 2
    return m
print('1.bisection')
print('root for interval [0,2] is : ',round(bisection(0,2, tol),5)) 
print('root for interval [-2,0] is: ',round(bisection(-2,0, tol),5))


# 0.9119186401367188
# -1.4318084716796875

def f(x):
    return x**2 + math.sin(x) - math.exp(x)/4 - 1


tol = 1e-5
def secant(x0, x1, tol):
    if abs(f(x0)) < abs(f(x1)):
        x0, x1 = x1, x0
    
    x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
    while abs(f(x2)) > tol:
        x0, x1 = x1, x2
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
    return x2

print('2.secant')
print('root for interval [0,2] is : ',round(secant(0,2, tol),5))
print('root for interval [-2,0] is: ',round(secant(-2,0, tol),5))



# -1.431808202233344
# 0.9119175181064569


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

print('3.newton')
print('root for interval [0,2] is : ',round(newton(0, tol),5))
print('root for interval [-2,0] is: ',round(newton(-2, tol),5))


# -1.4318086009771325
# 0.9119186162195468