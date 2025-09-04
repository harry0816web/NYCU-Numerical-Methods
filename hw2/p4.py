"""
linear system 
4.63 x1 – 1.21 x2 + 3.22 x3 = 2.22,
-3.07 x1 + 5.48 x2 + 2.11 x3 = -3.17,
1.26 x1 + 3.11 x2 + 4.57 x3 = 5.11.
"""
# def gauss_seidel_relax(A, b, x0, w):
#     tol = 1e-5
#     max_iter = 200
#     iter = 0
#     n = len(A)
#     x = x0[:]
#     while max_iter:
#         x_new = x[:]
#         for i in range(n):
#             sigma = 0
#             for j in range(n):
#                 if j != i:
#                     sigma += A[i][j] * (x_new[j] if j < i else x[j])
                           
#             x_new[i] = w/ A[i][i]  * (b[i] - sigma)   
#         if all(abs(x_new[i] - x[i]) < tol for i in range(n)):
#             break
#         x = x_new
#         max_iter -= 1
#         iter += 1
#     return [round(xi, 5) for xi in x], iter

def gauss_seidel_relax(A, b, x0, w):
    tol=1e-5
    max_iter=200
    iter = 0
    n = len(A)
    x = x0[:]
    while(max_iter):
        x_new = x[:]
        for i in range(n):
            sigma = 0
            for j in range(n):
                if j != i:
                    sigma += A[i][j] * (x_new[j] if j < i else x[j])
            x_new[i] = w * (b[i] - sigma) / A[i][i]
        if all(abs(x_new[i] - x[i]) < tol for i in range(n)):
            break
        x = x_new
        max_iter -= 1
        iter += 1
    return  [round(xi, 5) for xi in x], iter


mat = [
    [4.63, -1.21, 3.22],
    [-3.07, 5.48, 2.11],
    [1.26, 3.11, 4.57]
]

b = [2.22, -3.17, 5.11]

x0 = [0, 0, 0]  # Initial guess
# w values from 1.00 to 2.00, step 0.01
w_values = [0.01 * i for i in range(100, 200)]

min_iterations = float('inf')
best_omega = None
for w in w_values:
    sol, steps = gauss_seidel_relax(mat, b, x0, w)
    if steps < min_iterations:
        min_iterations = steps
        best_omega = w
    print(f"omega = {w:.2f}, iterations = {steps}, solution = {sol}")

print(f"Best omega: {best_omega:.2f} with {min_iterations} iterations")
