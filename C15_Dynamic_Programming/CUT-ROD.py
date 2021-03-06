import math


def cut_rod(p, n):
    if n == 0:
        return 0
    q = -math.inf
    for i in range(1, n + 1):
        q = max(q, p[i] + cut_rod(p, n - i))
    return q


def memoized_cut_rod(p, n):
    r = [-math.inf for _ in range(0, n + 1)]
    return memoized_cut_rod_aux(p, n, r)


def memoized_cut_rod_aux(p, n, r):
    if r[n] >= 0:
        return r[n]

    if n == 0:
        q = 0
    else:
        q = -math.inf
        for i in range(1, n + 1):
            q = max(q, p[i] + memoized_cut_rod_aux(p, n - i, r))
    r[n] = q
    return q


def bottom_up_cut_rod(p, n):
    r = [-math.inf for _ in range(0, n + 1)]
    r[0] = 0
    for j in range(1, n + 1):
        q = -math.inf
        for i in range(1, j + 1):
            q = max(q, p[i] + r[j - i])
        r[j] = q
    return r[n]


def extended_bottom_up_cut_rod(p, n):
    s = [-math.inf for _ in range(0, n + 1)]
    r = [-math.inf for _ in range(0, n + 1)]
    r[0] = 0
    for j in range(1, n + 1):
        q = -math.inf
        for i in range(1, j + 1):
            if q < p[i] + r[j - i]:
                q = p[i] + r[j - i]
                # s[j] holds the optimal size i of the first piece to cut off when solving a subproblem of size j.
                s[j] = i
        r[j] = q
    return r, s


def print_cut_rod_solution(p, n):
    r, s = extended_bottom_up_cut_rod(p, n)
    while n > 0:
        print(s[n])
        n = n - s[n]
