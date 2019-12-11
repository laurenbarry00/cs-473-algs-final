# Performs Knuth-Morris-Pratt search algorithm

# pattern: the pattern we're searching for
# txt: the text to be searched
def KMPSearch(pattern, text):
    # string lengths
    M = len(pattern)
    N = len(text)

    # lps = longest prefix suffix
    # lps[] holds the LPS values for each pattern
    lps = [0] * M

    # Calculate lps[] array
    computeLPSArray(pattern, M, lps)

    i = 0 # index for text[]
    j = 0 # index for pattern[]

    while i < N:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == M:
            return str(i - j)
            j = lps[j - 1]

        # Mismatch after j matches
        elif i < N and pattern[j] != text[i]:
            # Don't match lps[0 ... lps[j - 1]] characters,
            # as they will match anyways
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1


def computeLPSArray(pattern, M, lps):
    len = 0 # length of the LPS

    lps[0] # lps[0] is always 0
    i = 1

    # calculate lps[i] for i = 1 to M - 1
    while i < M:
        if pattern[i] == pattern[len]:
            len += 1
            lps[i]= len
            i += 1
        else:
            if len != 0:
                len = lps[len - 1]
            else:
                lps[i]= 0
                i += 1