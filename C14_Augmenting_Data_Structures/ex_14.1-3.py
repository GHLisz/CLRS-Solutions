def os_select(x, i):
    while True:
        if x.left is None:
            r = 1
        else:
            r = x.left.size + 1

        if i == r:
            return x
        elif i < r:
            x = x.left
        else:
            x = x.right
            i -= r
