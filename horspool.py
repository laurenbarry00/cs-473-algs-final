def ShiftTable(P, A):
    m = len(P)
    T = {}
    for i in range(0, len(A)):
        if A[i] not in P[0:m]:
            T[A[i]] = m
        else:
            T[A[i]] = m - 1 - i

    return T

def HorspoolSearch(P, X, A):
    T = ShiftTable(P, A)
    m = len(P)
    n  = len(X)
    i = m - 1
    while i <= n :
        k = 0
        while k <= m  and P[m - 1 - k] == X[i - k]:
            k = k + 1
        if k == m:
            return i - m + 1
        else:
            i = i + T[X[i]]
    return -1