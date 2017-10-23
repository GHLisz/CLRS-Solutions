def matrix_chain_multiply(A, s, i, j):
    if i == j:
        return A[i]
    if i+1 == j:
        return A[i] * A[j]
    b = matrix_chain_multiply(A, s, i, s[i, j])
    c = matrix_chain_multiply(A, s, s[i, j]+1, j)
    return b * c
