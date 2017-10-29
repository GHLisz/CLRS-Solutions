import math


def recursive_matrix_chain(p, i, j):
    if i == j:
        return 0
    m = math.inf
    for k in range(i, j):
        q = recursive_matrix_chain(p, i, k) \
            + recursive_matrix_chain(p, k+1, j) \
            + p[i-1]*p[k]*p[j]
        if q < m:
            m = q
    return m

