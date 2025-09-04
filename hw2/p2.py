def cal_tridiag(up, mid, down, b):
    n = len(mid)

    # forward elimination
    for i in range(1, n):
        mul = down[i] / mid[i-1]
        mid[i] = mid[i] - mul * up[i-1]    
        b[i] = b[i] - mul * b[i-1]

    # back substitution
    x = [0] * n
    x[-1] = b[-1] / mid[-1]
    for i in range(n-2, -1, -1):
        x[i] = (b[i] - up[i] * x[i+1]) / mid[i]

    return x


mid = [4,4,4,4,4,4]
up = [-1,-1,-1,-1,-1,0]
down = [0,-1,-1,-1,-1,-1]
b = [100,200,200,200,200,100]

x = cal_tridiag(up, mid, down, b)
print("Solution:")
for i in range(len(x)):
    print(f"x{i} = {x[i]}")