def minimum(A):
    m = A[0]
    for val in A:
        if m > val:
            m = val
    return m

if __name__ == '__main__':
    a = [1, 3, 5, 4, 6]
    print(minimum(a) == 1)
