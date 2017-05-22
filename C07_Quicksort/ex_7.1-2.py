def partition(A, p, r):
    x = A[r - 1]
    i = p - 1
    for k in range(p, r - 1):
        if A[k] < x:
            i += 1
            A[i], A[k] = A[k], A[i]
    i += 1
    A[i], A[r - 1] = A[r - 1], A[i]
    j = i
    for k in range(i + 1, r):
        if A[k] == x:
            j += 1
            A[j], A[k] = A[k], A[j]
        k -= 1
    return (i + j) // 2
