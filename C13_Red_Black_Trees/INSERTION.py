RED = True

def rb_insert(T, z):
    y = T.nil
    x = T.root
    while x != T.nil:
        y = x
        x = x.left if z.key < x.key else x.right
    z.p = y
    if y == T.nil:
        T.root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z
    z.left = T.nil
    z.right = T.nil
    z.color = RED
    rb_insert_fixup(T, z)


def rb_insert_fixup(T, z):
    while z.p.color == RED:
        if z.p == z.p.p.left:
            y = z.p.p.right
            pass
