"""
linear system 
4.63 x1 – 1.21 x2 + 3.22 x3 = 2.22,
-3.07 x1 + 5.48 x2 + 2.11 x3 = -3.17,
1.26 x1 + 3.11 x2 + 4.57 x3 = 5.11.
"""
def jacobi(A, b, x0):
    tol = 1e-5
    max_iter = 200
    n = len(A)
    x = x0[:]
    while(max_iter):
        x_new = x[:]
        for i in range(n):
            sigma = 0
            for j in range(n):
                if j != i:
                    sigma += A[i][j] * x[j]
            x_new[i] = (b[i] - sigma) / A[i][i]
        if all(abs(x_new[i] - x[i]) < tol for i in range(n)):
            break
        x = x_new
        max_iter -= 1
    return [round(xi, 5) for xi in x]

def gauss_seidel(A, b, x0):
    tol=1e-5
    max_iter=200
    n = len(A)
    x = x0[:]
    while(max_iter):
        x_new = x[:]
        for i in range(n):
            sigma = 0
            for j in range(n):
                if j != i:
                    sigma += A[i][j] * (x_new[j] if j < i else x[j])
            x_new[i] = (b[i] - sigma) / A[i][i]
        if all(abs(x_new[i] - x[i]) < tol for i in range(n)):
            break
        x = x_new
        max_iter -= 1
    return [round(xi, 5) for xi in x]


mat = [
    [4.63, -1.21, 3.22],
    [-3.07, 5.48, 2.11],
    [1.26, 3.11, 4.57]
]

vec = [2.22, -3.17, 5.11]

x0 = [0, 0, 0]  # Initial guess
solution = jacobi(mat, vec, x0)
solution2 = gauss_seidel(mat, vec, x0)

print("Solution by jacobi:")
for i in range(len(solution)):
    print(f"x{i} = {solution[i]}")

print("Solution by gauss_seidel:")
for i in range(len(solution2)):
    print(f"x{i} = {solution2[i]}")
