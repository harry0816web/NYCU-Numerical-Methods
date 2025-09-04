def inf_norm(matrix):
    maxn = 0
    for row in matrix:
        for x in row:
            maxn = max(maxn, abs(x))
    return maxn

def identity_matrix(n):
    I = []
    for i in range(n):
        row = [0] * n
        row[i] = 1
        I.append(row)
    return I

def inverse_matrix(A):
    """使用高斯-喬登消去法求反矩陣，假設 A 是非奇異方陣"""
    n = len(A)
    A = [row[:] for row in A]  # 複製避免修改原始矩陣
    I = identity_matrix(n)

    for i in range(n):
        # 先除掉 pivot
        pivot = A[i][i]
        for j in range(n):
            A[i][j] /= pivot
            I[i][j] /= pivot
        # 將其他列變成 0
        for k in range(n):
            if k != i:
                factor = A[k][i]
                for j in range(n):
                    A[k][j] -= factor * A[i][j]
                    I[k][j] -= factor * I[i][j]
    return I

def condition_number(matrix):
    norm_A = inf_norm(matrix)
    A_inv = inverse_matrix(matrix)
    norm_A_inv = inf_norm(A_inv)
    cond = norm_A * norm_A_inv
    classification = "well-conditioned" if cond < 1e3 else "ill-conditioned"
    return cond, classification

mat = [[10^10,0],[0,10^-10]]
print(condition_number(mat))
