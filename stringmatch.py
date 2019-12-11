# Test cases for Horspool, KMP, and Rabin-Karp Algorithms

# import the algorithms from their respective files
import horspool
import kmp
import rabinkarp

# create a test case
# txt = "some string"
# pat = "str"

# run the test case against the algorithms
# print(kmp.KMPSearch(pat.txt))
# print(rabinkarp.RabinKarpSearch(pat, txt))
# print(horspool.HorspoolSearch(pat, txt, len(txt)))


txt = "ABABDABACDABABCABAB"
pat = "ABABCABAB"
print(kmp.KMPSearch(pat, txt))