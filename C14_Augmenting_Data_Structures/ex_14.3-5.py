def interval_search_exactly(T, i):
    x = T.root

    while x != T.nil and x.int.low != i.int.low:
        if x.int.low > i.int.low:
            x = x.left
        else:
            x = x.right

    if x != T.nil and x.int.high != i.int.high:
        return T.nil

    return x
