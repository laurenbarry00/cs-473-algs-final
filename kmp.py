# Performs Knuth-Morris-Pratt search algorithm
# pat: the pattern we're searching for
# txt: the text to be searched
# 
def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)

    # lps = longest prefix suffix
    # lps[] holds the LPS values for each pattern
    lps = [0] * M

    # Calculate lps[] array
    computeLPSArray(pat, M, lps)

    i = 0 # index for txt[]
    j = 0 # index for pat[]

    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1

        if j == M:
            return str(i - j)
            j = lps[j - 1]

        # Mismatch after j matches
        elif i < N and pat[j] != txt[i]:
            # Don't match lps[0 ... lps[j - 1]] characters,
            # as they will match anyways
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1


def computeLPSArray(pat, M, lps):
    len = 0 # length of the LPS

    lps[0] # lps[0] is always 0
    i = 1

    # calculate lps[i] for i = 1 to M - 1
    while i < M:
        if pat[i] == pat[len]:
            len += 1
            lps[i]= len
            i += 1
        else:
            if len != 0:
                len = lps[len - 1]
            else:
                lps[i]= 0
                i += 1

txt = "ABABDABACDABABCABAB"
pat = "ABABCABAB"
print(KMPSearch(pat, txt))