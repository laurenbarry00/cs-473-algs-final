NUM_OF_CHARS = 256

def getBadChar(string, size):
    # init all as -1
    badChar = [-1]*NUM_OF_CHARS

    # fill in values of last occurence
    for i in range(size):
        badChar[ord(string[i])] = i;

    return badChar

def BoyerMooreSearch(pattern, text):
    m = len(pattern)
    n = len(text)

    # bad character list
    badChar = getBadChar(pattern, m)

    s = 0 # s = shift
    while(s <= n - m):
        j = m - 1

        # keep reducing j while characters of pattern and text are matching at the current shift s
        while j>=0 and pattern[j] == text[s+j]:
            j -= 1

        # if the pattern is present, j = -1
        if j<0:
            return s
        # shift pattern so the bad character aligns with the last occurence of it in the pattern
        else:
            s += max(1, j - badChar[ord(text[s + j])])
