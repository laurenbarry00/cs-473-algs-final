#Based on code from https://www.geeksforgeeks.org/rabin-karp-algorithm-for-pattern-searching/

def RabinKarpSearch(pattern, text):
    count = 0
    q = 7 # a prime number
    d = 256 # num. of characters input alphabet

# string lengths

    M = len(pattern)

    N = len(text)

 # hash value for pattern and text

    hp = 0

    ht = 0

    h = 1

    i = 0 

    j = 0



    # h = pow(d, M-1) % q

    for i in range(M - 1):

        h = (h * d) % q



    # calculate hash value of pattern and the first window of text

    for i in range(M):

        hp = (d * hp + ord(pattern[i])) % q

        ht = (d * ht + ord(text[i])) % q



    # slide pattern over text, one by one

    for i in range(N - M + 1):

        # check if the hash values are the same. only then check the characters 

        if hp == ht:

            for j in range (M):
                if text[i + j] != pattern[j]:
                    break;



            j += 1



            if j == M:
                print ("index of pattern is", i)
                return i



        if i < N - M:

            ht = (d *(ht - ord(text[i]) * h) + ord(text[i + M])) % q

            if ht < 0:

                ht = ht + q
    print("Rabin-Karp: Not found.")
    return -1


