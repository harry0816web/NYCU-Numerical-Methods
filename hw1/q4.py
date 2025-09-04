import math
import numpy as np
def jac(x0):    # return J(x0)
    jac = []
    jac.append([1,-3,-2*x0[2]])
    jac.append([6 * (x0[0]**2),1,-10 * x0[2]])
    jac.append([8*x0[0],1,1])
    return jac

def f(x0):      # return - f(x0)
    f = []
    f.append(x0[0] - 3*x0[1] - x0[2] ** 2 + 3)
    f.append(2*x0[0]**3 + x0[1] - 5*(x0[2]**2) + 2)
    f.append(4 * (x0[0] ** 2) + x0[1] + x0[2] - 7)
    for i in range(len(f)):
        f[i] = f[i] * -1

    return f

def partial_pivoting(J,pivot):  
    n = len(J)
    for i in range(pivot,n):
        max = i
        for j in range(i+1, n):
            if abs(J[j][i]) > abs(J[max][i]):
                max = j
        if max != i:
            J[i], J[max] = J[max], J[i]
    return J

def newton(x0, tol):
    while abs(f(x0)[0]) > tol or abs(f(x0)[1]) > tol or abs(f(x0)[2]) > tol:
        x1 = [0,0,0]

        # J(x0)*s = -f(x0)
        # to solve s, do the gaussian elimination for [J(x0) | -f(x0)]

        J = jac(x0)
        # append constant term of f(x0) to J
        J[0].append(f(x0)[0])
        J[1].append(f(x0)[1])
        J[2].append(f(x0)[2])

        # first row
        # J = partial_pivoting(J, 0)
        for i in range(1, 3):
            # m = J[1][0] / J[0][0] XXXXXXXX
            m = J[i][0] / J[0][0]   # 每次都計算新的 m!!!!!!!
            for j in range(0, 4):
                J[i][j] = J[i][j] - m * J[0][j]

        # second row
        # J = partial_pivoting(J, 1)
        m = J[2][1] / J[1][1]  
        for j in range(1, 4):     
            J[2][j] = J[2][j] - m * J[1][j]

        s = [0,0,0]
        s[2] = J[2][3] / J[2][2]
        s[1] = (J[1][3] - J[1][2]*s[2]) / J[1][1]
        s[0] = (J[0][3] - J[0][2]*s[2] - J[0][1]*s[1]) / J[0][0]
        x1 = [x0[0] + s[0], x0[1] + s[1], x0[2] + s[2]]
        x0 = x1
    return x0


# test
tol = 1e-5
ans = []
ans.append([np.round(x,5) for x in newton([1.0,1.0,1.0], tol)])
ans.append([np.round(x,5) for x in newton([1.3,0.9,-1.2], tol)])
for i in range(8):          
    v = [10000 + 1j,10000 + 1j,10000 + 1j]
    # try every possible combination of 1 and -1
    if i & 1:
        v[0] = -10000 + 1j
    if i & 2:
        v[1] = -10000 + 1j
    if i & 4:
        v[2] = -10000 + 1j
    #round the answer to 5 decimal places
    res = [np.round(x,5) for x in newton(v, tol)]
    if res not in ans:
        ans.append(res)
for a in ans:
    print('sol: ',a)



