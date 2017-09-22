RED = True
BLACK = False


class Node:
    def __init__(self, key):
        self.key = key
        self.color = BLACK
        self.p = None
        self.left = None
        self.right = None


class Tree:
    def __init__(self, root=None):
        self.root = root


def rb_transplant(T, u, v):
    if u.p == T.nil:
        T.root = v
    elif u == u.p.left:
        u.p.left = v
    else:
        u.p.right = v
    v.p = u.p


def tree_minimum(x):
    while x.left is not None:
        x = x.left
    return x


def rb_delete(T, z):
    y = z
    y_original_color = y.color
    if z.left == T.nil:
        x = z.right
        rb_transplant(T, z, z.right)
    elif z.right == T.nil:
        x = z.left
        rb_transplant(T, z, z.right)
    else:
        y = tree_minimum(z.right)
        y_original_color = y.color
    x = y.right
    if y.p == z:
        x.p = y
    else:
        rb_transplant(T, y, y.right)
        y.right = z.right
        y.right.p = y
    rb_transplant(T, z, y)
    y.left = z.left
    y.left.p = y
    y.color = z.color
    if y_original_color == BLACK:
        rb_delete_fixup(T, x)


def rb_delete_fixup(T, x):
    pass
