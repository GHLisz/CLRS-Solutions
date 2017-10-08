def intervals_search(T, i):
    x = T.root
    ret = []

    while x != T.nil:
        if x.int.low <= i.int.high and x.int.high >= i.int.low:
            ret.append(x)

        if x.left != T.nil and x.left.max >= i.low:
            x = x.left
        else:
            x = x.right

    return ret
