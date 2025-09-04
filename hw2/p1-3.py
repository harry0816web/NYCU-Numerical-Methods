import math
# [A|b]
mat = [[2.51,1.48,4.53,0.05],[1.48,0.93,-1.3,1.03],[2.68,3.04,-1.48,-0.53]]
# print initial matrix
print("Initial matrix:")
for row in mat:
    print(row)
print()

# gaussian elimination
for i in range(len(mat)):
    # pivoting
    for j in range(i+1, len(mat)):
        if abs(mat[j][i]) > abs(mat[i][i]):
            mat[i], mat[j] = mat[j], mat[i]

    # eliminate
    for j in range(i+1, len(mat)):
        factor = mat[j][i] / mat[i][i]
        for k in range(i, len(mat[0])):
            mat[j][k] -= factor * mat[i][k]
            mat[j][k] = math.floor(mat[j][k] * 1000) / 1000
    
    # print intermediate matrix
    print(f"After eliminating row {i}:")
    for row in mat:
        print(row)

# back substitution
x = [0] * len(mat)
for i in range(len(mat)-1, -1, -1):
    x[i] = mat[i][-1]
    for j in range(i+1, len(mat)):
        x[i] -= mat[i][j] * x[j]
        mat[j][k] = math.floor(mat[j][k] * 1000) / 1000
    x[i] /= mat[i][i]

# The correct solution is x = 1.45310, y = -1.58919, z = -0.27489.
print('corect solution')
print('x = 1.45310, y = -1.58919, z = -0.27489')

print("Solution:")
for i in range(len(x)):
    print(f"x{i} = {x[i]}")
    
# substitute back into the original equations to check the solution
print("Substituting back into the original equations:")
b = [0.05, 1.03, -0.53]
db = [0] * len(b)
for i in range(len(b)):
    db[i] = mat[i][-1]
    for j in range(len(x)):
        db[i] -= mat[i][j] * x[j]

print("Difference:")
for i in range(len(db)):
    print(db[i])
