import numpy as np

# 題目給的資料
x = np.array([0.40, 1.2, 3.4, 4.1, 5.7, 7.2, 9.3])
y = np.array([0.70, 2.1, 4.0, 4.9, 6.3, 8.1, 8.9])
z = np.array([0.031, 0.933, 3.058, 3.349, 4.870, 5.757, 8.921])

# (A^T A) a = A^T b
A = np.vstack([x, y, np.ones_like(x)]).T  
b = z                                     

# A^T A = A^T b
ATA = A.T @ A    
ATb = A.T @ b     

# 解x
x = np.linalg.solve(ATA, ATb)
a, b_coeff, c = x

print(f"res: z = {a:.5f} x + {b_coeff:.5f} y + {c:.5f}")

# residuals
z_pred = A @ x
residuals = z - z_pred
SSE = np.sum(residuals**2)

print(f"sum of the squares of the deviations:  {SSE:.5f}")
