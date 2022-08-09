# A[m, n], B[n, o], result[m, o]
m = 3
n = 4
o = 2

A = [[0]*n]*m
B = [[0]*o]*n
result = [[0]*o]*m

# T: O(n^3), S:O(n^3)
for i in range(0, len(A)):
    for j in range(0, len(B[0])):
        for k in range(0, len(B)):
            result[i][j] += A[i][k] * B[k][j]

print(result)