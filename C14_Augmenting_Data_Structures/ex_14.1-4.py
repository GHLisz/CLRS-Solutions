def os_key_rank(x, k, i=0):
    r = 1
    if x.left is not None:
        r += x.left.size

    if k == x.key:
        return i + r
    if k < x.key:
        return os_key_rank(x.left, k, i)
    if k > x.key:
        return os_key_rank(x.right, k, i+r)
