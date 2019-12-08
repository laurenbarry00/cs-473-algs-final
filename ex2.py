def ShiftTable(P, A):
    m = len(P)
    T = {}
    for i in range(0, len(A)):
        if A[i] not in P[0:m]:
            T[A[i]] = m
        else:
            T[A[i]] = m - 1 - i

    return T

def Horspool(P, X, A):
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

#Based on code from https://www.geeksforgeeks.org/rabin-karp-algorithm-for-pattern-searching/
def RabinKarp(D, P, X):
    q = 7
    m = len(P)
    n = len(X)
    hp = 0
    hx = 0
    h = 1
    for i in range(0, m ):
        h = (h * D) % q
        i = i + 1
    for j in range(0, m ):
        hp = (D * hp + ord(P[j])) % q
        hx = (D * hx + ord(X[j])) % q
        j = j + 1
    for k in range(0, n - m + 1 ):
        if hp == hx:
            match = True
            for l in range (0, m ):
                if X[k + l] != P[l]:
                    match = False
            if match == True:
                return k
        if k < n - m :
            hx = (D *(hx - ord(X[k]) * h) + ord(X[k + m])) %q
        if hx < 0:
            hx = hx + q
    return -1


A = ['A', 'C', 'G', 'T']
P = 'ACT'
X = 'CCACTACTGGGGACTCTT'
print(Horspool(P, X, A))
print(RabinKarp(4, P, X))