#Horspool algorithm based on pseudocode from pg. 261-262 of
#Introduction to Algorithm Design and Analysis by Levitin
def ShiftTable(P):
    #P is the pattern
    #A is the alphabet
    A = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G'
    , 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm',
    'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't',
    'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z', '1', '2',
    '3', '4', '5', '6', '7', '8', '9']
    m = len(P)
    T = {} #T is the table for the shifts
    for i in range(0, len(A)):
        if A[i] not in P[0:m]: #last letter doesn't match so shift
            #by entire pattern length
            T[A[i]] = m
        else:
            if m - 1 - i > 0:
                T[A[i]] = m - 1 - i
            else:
                T[A[i]] = 1

    return T


def HorspoolSearch(P, X):
    count = 0

    T = ShiftTable(P)

    m = len(P)

    n  = len(X)  #X is the text

    i = m - 1

    while i <= n :

        k = 0

        while k < m  and P[m - 1 - k] == X[i - k]:
            count = count + 1 #increment until length of pattern is reached
            #or a mismatch is found
            k = k + 1

        if k == m:
            return i - m + 1  #found a match

        else:

            i = i + T[X[i]]
    print("Horspool: Not found")
    return -1
