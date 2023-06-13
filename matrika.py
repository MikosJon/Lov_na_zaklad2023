def zmnozi_matriki(A, B):
    n = len(A)
    C = [[None] * n for _ in range(n)]
    print(C)
    for i in range(n):
        for j in range(n):
            C[i][j] = sum(A[i][k] * B[k][j] for k in range(n))
    return C