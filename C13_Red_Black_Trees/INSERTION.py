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
    # 违反了性质 4 才循环
    # 不可能有多个节点时插入到根结点，因此性质 2 不会违反
    while z.p.color == RED:
        # 根据 z.p 是 z.p.p 的左右结点分为两种情况
        if z.p == z.p.p.left:
            # y 为 z.p 的兄弟结点
            y = z.p.p.right
            # 情况一，z 的叔叔结点也是红色
            if y.color == RED:
                # 直接把父节点设置为黑色
                z.p.color = BLACK
                # 为了保护性质 5 把另外两个也改了
                y.color = BLACK
                z.p.p.color = RED
                # z 向上挪到红色结点
                # 这里结束之后可能违反性质 5 也可能违反性质 2，但不会同时违反
                z = z.p.p
            # 情况二，z 的叔叔结点是黑色并且 z 是右孩子
            elif z == z.p.right:
                # 直接左转变成情况三，当然 z 要向上移动一位
                z = z.p
                left_rotate(T, z)
            # 情况三，z 的叔叔结点是黑色并且 z 是左孩子
            # 直接把父节点设置为黑
            z.p.color = BLACK
            # 为了保护性质 4 祖父结点设置为红
            z.p.p.color = RED
            # 为了保护 z 叔叔结点一侧的性质 5，向右旋转
            # 这样 z.p 一定是黑了
            right_rotate(T, z.p.p)
        else:
            y = z.p.p.left
            if y.color == RED:
                z.p.color = BLACK
                y.color = BLACK
                z.p.p.color = RED
                z = z.p.p
            elif z == z.p.left:
                z = z.p
                T.right_rotate(z)
            z.p.color = BLACK
            z.p.p.color = RED
            T.left_rotate(z.p.p)
    # 如果直接在跟结点插入
    # 那么原来树为空
    # 此时违反了性质 2，于是这里改过老
    T.root.color = BLACK


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
