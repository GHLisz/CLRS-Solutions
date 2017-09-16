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
