def interval_search(T, i):
    x = T.root

    while x != T.nil and (i.int.high < x.int.low or x.int.high < i.int.low):
        if x.left != T.nil and x.left.max >= i.low:
            x = x.left
        else:
            x = x.right

    return x
