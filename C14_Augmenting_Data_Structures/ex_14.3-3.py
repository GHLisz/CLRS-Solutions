def min_low_endpoint_interval_search(T, i):
    x = T.root

    ret = T.nil

    while x != T.nil:
        if not (i.int.high < x.int.low or x.int.high < i.int.low):
            if ret == T.nil or ret.int.high > x.int.high:
                ret = x

        if x.left != T.nil and x.left.max >= i.low:
            x = x.left
        else:
            x = x.right

    return ret
