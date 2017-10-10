import math


def cut_rod(p, n):
    if n == 0:
        return 0
    q = -math.inf
    for i in range(1, n+1):
        q = max(q, p[i] + cut_rod(p, n-i))
    return q
