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
    while x != T.root and x.color == BLACK:
        if x == x.p.right:
            w = x.p.right
            if w.color == RED:
                w.color = BLACK
                x.p.color = RED
                left_rotate(T, x.p)
                w = x.p.right
            if w.left.color == BLACK and w.right.color == BLACK:
                w.color = RED
                x = x.p
            else:
                if w.right.color == BLACK:
                    w.left.color = BLACK
                    w.color = RED
                    right_rotate(T, w)
                    w = x.p.right
                w.color = x.p.color
                x.p.color = BLACK
                w.right.color = BLACK
                left_rotate(T, x.p)
                x = T.root
        else:
            pass
    x.color = BLACK


def left_rotate(T, x):
    y = x.right

    x.right = y.left
    if y.left:
        y.left.p = x

    y.p = x.p
    if not x.p:
        T.root = y
    elif x == x.p.left:
        x.p.left = y
    else:
        x.p.right = y

    y.left = x
    x.p = y


def right_rotate(T, y):
    x = y.left

    y.left = x.right
    if x.right:
        x.right.p = y

    x.p = y.p
    if not y.p:
        T.root = x
    elif y == y.p.left:
        y.p.left = x
    else:
        y.p.right = x

    x.right = y
    y.p = x
