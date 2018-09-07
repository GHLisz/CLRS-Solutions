def os_select(x, i):
    r = x.left.size + 1
    if i == r:
        return x
    elif i < r:
        return os_select(x.left, i)
    else:
        return os_select(x.right, i - r)


def os_rank(T, x):
    r = x.left.size + 1
    y = x
    while y != T.root:
        if y == y.p.right:
            r = r + y.p.left.size + 1
        y = y.p
    return r
