def os_key_rank(x, k):
    if k == x.key:
        return x.left.size + 1
    elif k < x.key:
        return os_key_rank(x.left, k)
    else:
        return os_key_rank(x.right, k) + x.left.size + 1
