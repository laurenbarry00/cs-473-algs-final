# Test cases for Horspool, KMP, and Rabin-Karp Algorithms

# for measuring the execution time
import timeit

# ----- Test Cases -----
# Length 10
text10 = "XxfRnW7yPQ"
pattern10 = "fRnW"

# Length 100
text100 = "AnL2a8U9dPdmXFDxxqtiL0304mRSFEBlgM3RBiCyHvKv1JyEJyv4JCTC4ExrlSX12f2y6BOtCfluWiGCWuzA5GSZQWSDzhBKy7HX"
pattern100 = "uWiGCWuzA5"

# Length 200
text200 = "e3y7cKdzq86vmrps4ZPTmJCFVLT0o5zQJ0kztRCASgWAhitnrkDdAEIhOeAZPUj2RGALSbIYipMCEPfJKxdzG4iFOfZfZB9RAeSVPE1ITjm8tFBivpwUCaFiKMRPAuqsOoigH6pp6560B0jZTFY93A3xTsUksyOUMS9J1Z4h3eoMAQrL8WBnHEGb0iM2M9iqUfpZm5Ld"
pattern200 = "FOfZfZB9RAeSVPE1ITjm8tFBiv"

# Length 300
text300 = "KNP9yWKOnwesENUfOCZGIvjs4fdc0yOIcsN3kDG7wCiw4SGysuRE5Xw7vUc8RdupUwrTlmi8xBIg3GqpDFk2NdjMkLsuQxq331JYPIrWl0vp8lcaHGiUrImxS7ZyX9XfB28o8y55gAjcShRF8Zqt7yuYTXS0nUCLMrgJG46cCYI9431HJHgOaV8ukSVXLajJzkDa90XNkWjb0RsqBLRSncIIGJmJpaOhzeOQ1ALwUzlrRY27PqX4N27w3DDD9zIgqOJJRWfJESZZeK4hiKg6By9qjYjyF52ti1CAWvxxMDb0"
pattern300 = "iKg6By9qjYjyF52ti1CAWvxxMDb0"

# Length 400
text400 = "HfuQ48pEuANr8PKCw2OIXHgmPMoTjvgK8VvGzpT8Pe47NEK0JNPIpQkuoRnKeaabBMqG0BnjhLcgpn5LkY6r6RlUulVmOhgxdD7HjFV95SI0vpZ9RHBr7sUVrRjB8BRas0w7kCJYHO7hr3tlRuGnNeaTKIWLXSBiMdA99g1DqQt3gtbZ4nGH2tm0NW53GQWmL1FQkDc1wA5gVHakqikXHuPfjGPGWuTOJQUeQsB8WI9AL94asgzBXMxKX5B0oTc8ncetBQx57zlB9ryiF6JARZflbPBn77AkkkfSi1ShOr8mE4NNlwIEzlWt7AbJaJTH0vWO8VgyPr3saciQ2zEtsYhjttI3Otkc4vpknL7MLd5Y0IQR14vf8NRo5VxqgRzyVWdI1JVBQ1SB7JF8"
pattern400 = "0vWO8VgyPr3saciQ2zEtsYhjttI3Otkc4vpknL7MLd5Y0IQR1"

# Length 500
text500 = "adCIAtMoaouiTWCCbKLaP5fb2WThvo0n359cOeE4hdZARBZFawpEFFG8Uy991TIMfRFZyktnAHVanyXNd4uOwGv5sI3xQ3G5VThzqdgc32Qjivf4EicpdiK8SxHhB3a2dYJToDSzZinw6bHNNF9AoInPEyHggXKJyC9sGnvQFtzLp2eRwbqVkrv5vWQ3NRT4nwZCgMSpCJFq7XiZqFprRM3SkVDrJQt3DUeTqkkg9NjRUSWSliM9gS1ua6mNpzkIkkHubDH7fV46j4ohwFfB1P3tu7FRzvt5xzdIBrKltEHSyqSRasH84xRaQGEOvSrZXFOfzNSbxQZq5ZdUAajxnE2k8zEDqrYCBn4ok7aR0PsnhqQPuPkpIExw9yzXkDGCq3aZmNcVPllcQrO5WjGF7yHbr8CMBNlgcMl9X3EDpzETsA8bCpa4Fc3Uj1ln7JnFF4vCGYQULXivoOuJspC8GfoZ8Fxsieq6hQRdSA0CnE51ZAnPg9bX"
pattern500 = "F4vCGYQULXivoOuJspC8GfoZ8Fxsieq6hQRdSA0CnE51Z"

# Length 600
text600 = "0wyCAfzhMhRsKGBo255GIcRcp5CfVBfCTJIkUyq8bj41WoBumunUefiI2giY6d6toRl923LjHVfg4XrvCiUmooZxg1wm8cG1X9njw8zKHK8aZP7ktTT0iEgxNo4V3nyCVA03qTJdgHzciGJT7XR1C0M9vbmIqk6Lg5DfzEOVJDyGrUUNotBPEdZPJwD72lMGJLZvSs2fqDP9Rp100gtKw7IacPuNvcBnsEuua1WDXReMGJdhcAyfIoX3TV681jpU4fGjGGX0GfpwL2ivFe6e5zWDhhFLkHuqCm2yEOJmLBjmZHeDmJYo83MeP1VrEPpRJtVXTMzobu1iqHxPPCLEo7UsVy2ciYbN4w8ydBhupD53V2EiE3lOAUlSMadFlEIA1f2cdZsbT4lxTSFP7SZ5TIZ36rjl2nQOTKjsG7by4Y8JXRH0etje6FESbWOOFlHikxqjFVmgchm6QD1xYCO0Crf8eBuu7QgAqdtsnarcK3g6x2RdcZ12cSw0sLAUQOQBzvdDnDHa4sD5dNdaN4n2BjfnEyJ67ErctD6Zxs4vlfO6w4hPaoCbqt958ulmIyczkhF3rMJN1JJoebbBYUHbACAs"
pattern600 = "QgAqdtsnarcK3g6x2RdcZ12cSw0sLAUQOQBzvdDnDHa"

# Length 700
text700 = "nsuxfXtUnq6S7X0lCeW8JFKtvtaVugjwcg97GuYHg1QiZaS35SK0oAoRH9PEyfD5RmHNZ62qybGATh9JeDYk5c1RQZSk9FZAojdtNcuHkS2bhSzLq9jkyxxeRc3xlHwSDWVnAZ1uvJ8KfpdNEnLJ3XbanBP1kO5li7cwrWSwnmZZU0DjalqIBnCZlF93dA1mJOiZbRt19VAnRajLIsK7pJnCYewC4Vw4HnbFLIp1SgfP5z8Xe1OR46URrfZnCNUTykgVkkSL7hHOPc7fVDA5afVd7m3TPUrxeJ6GABj2Do2RylqDVZOXxpiLbzeI55ISD6dxo4pYUxJYifTNA91N0fZQsTz85YTBgLID7H2fHhVcS1L6P4eBK6AygLjODnMi35jMNkQ7tsGp0URJZC5b7qKfzkmkwCWoDnNzqiW8TmUqJ0M2Ak54DIDucYftf7dYOdZrScE05K2txTf48H0YwOavXlgiW7ozY7eTypvdIc8xkhG59tBQ3HiNvh6qS9bTht4E8UoVTIA87RSZNF7otNDXwDXWW3UkbexTevskLUxGLYDYauWqQzoiQXXA2ZngXqySFqixBznkDxtu367ydAboZ9EYsftnaOnqydgsh2Q3q1tPAHgWVT9xoRy0gB1kv695gPhrypTtyYgtSZ5j7S6TpUmIZ8tpObQ9KBJwlTCeCNcTClBEVLwtjBdG"
pattern700 = "UxJYifTNA91N0fZQsTz85YTBgLID7H2fHhVcS1L6P4"

# Length 800
text800 = "ATKB6Pt6fspLxX9JGVj2T3NaObzoNx1E3zV91NYrKTtQIsop8CPAoPxJg8HjSfYmM5hGSpQXiQjyLwu5iQSjJ0GOz02i9gJ45EgjVRIm9pnPdOdtRQrLtKuy19HIzkSkqjCAG0yNzKIqnmpMi2BBdevu2YlAbp5VvKN7TL10nb9IU3oyGN4YaChpT6ewLRUoWclJOECaQstws8ROOR3JucTlUR39VQZ6Z4dYS3DYHiIelTMcvDnvVFozZ42W4mEwRNyQcAEvNl0hKopRt2J2S3yMUpmx5yb3zi4UhXiwPDZt05D02wvcFBtwiusE6Fse7njS4P2gmqsCX5TT9FegLtjj4vUmoaV2w1rTrSGeaDGCDkW6bVJijF6l4wqHyGPB4U6qemcsoie1Q5yIoayBuW5Ts6xItvGpeG8n0tpL8AXsKIeSugP1IoYP0HOfb8N4W5qAf2kvLaQU7afqcpBP6BO2OYniy7KzqPQP41FzR0TpPVETibTwWWTl6lcbUkHMbBGI0drffgcQVwfDmWmWahHGhd6HJexWvfWgatJ712EPfw3VwlPrXNyrDjbeGdP6lL67fE3LGYfWsA79uH4e2x3oT5UO8XbQtXvgmkclQucy5JkA7c5LDQbBAo7dcqADidH8RP0yEJAb9bwW9P8JSYzSVBoL5ULIl6KEsXBCffI8C1lmzXAK7Iza2lkG1VvzP7WTm1FrAm9yDhSHVYsGb7hINKmDCH6aHqNVD1Eqwbr0MEaLUyPwP3q9EMqJZrfKFltEGiOn4Os9z8fPwcBfaZxUuLCZQiDs"
pattern800 = "E3LGYfWsA79uH4e2x3oT5UO8XbQtXvgmkclQucy5JkA7c"

# Length 900
text900 = "Vper83e9c7oxzBM1lfJiDYwaQzHNNh7TM37TRBkP1e1G4gbjGpBadiSTslLI25WCICqDFX52XsWpj86927CuUt24Ryu1tTogl3HmSAgoONRGc1SSxwmUExlXtq9BO5WpfE2huw4d4kzgFrQ1QI9T4ByDePMw2oQldvP5TIjJZYRpKfwy2BsAicGl8TlSxapw2O1GVyfc7MRuPG4l7DZ0HiyONsz9MbN6ujA9z9KjAM51iVgtdeOTOcDLk5r7WVPvxWsAJir6VrElkrCym8c6Ev4svPoniTu5U7q1HAbLKze6Lh0r7taiJ3BNee6hd7fAWo0BFal9SB11ZmS6vtPg3Ri6BykuxJFt9oSKX3xtNyQESt807RVCAxv8mPiLmjoTVAmCQJ2Y734Gj0bBYu5cLMF28O0iR4p38mUdfi6QCp8zH9E5ytT840UVosq7zgCTc3nfmImVAqKoTUAQh01uLjnhD0Ne6fFLXMVY4hmDvvdTv6h3O5PNzbcoSTezJosRsFWrbhSEmIhT5PzWTsrXqSEkDSE567buIzsnC7VoWBoxS3xA2CJoFMhUEN0hM27UhRhA3yqzuXnLUERRONizEPlUyHRtyuECPFp8kajhubxHYKdmxausAQ2dophRfDF25zxqoLvqRIrqRjIojIX9ZUaXdlP6WK4uLWq1B5cGGt1GghzVWXSCXIZP2kquZakR9951xnCoHxaYXPaXPQdDIywAdsidDeU3RfsjDtCRbEfKiwVvtaGdpgq07DxNu46Ls4HwSvJMaoS1KJAXYdFZpQ0D6UMxQ86U8M1XioXGe0BjLzdx7LhFwHcr0AEN6cwth2EKrG0Ki6OQ09kfZTt3VQ8SlNdjewJ2LX5LeaZ6o5LT5Ggimp1pvxVgXfUA9hdHEPUs"
pattern900 = "iwVvtaGdpgq07DxNu46Ls4HwSvJMaoS1KJAXYdFZpQ0D6UM"

# Length 1000
text1000 = "pAgNvne12qXEQElC2fQg3ha8hOEevwIfGGrZAIjbSHQOARzliV12tg3O67PxuWX3AyvDOTV5lhZIlnC1MvsrrP3hqsiltWMFmkoOqXEl9qCBeGgJLqO74G7nMZh89pXV4XLqqoME6BECPHcM9mDsEu5myN6UCUbkPczpSf2dzM5tIEigngi2iI10weOTN67IZMVzTYhEe2wPpIrqCr5NXOXxGpxRoIfJZdnmHi1I1d680IIsmpAMPNppzSaat9VYKeHvyihSCv9Nt6C0uItebky0CTfcZYXRd13DbWb2Y469dPmYeuMFyKxgLCcQpsvPGrP9a0ayiCqmgXmUj6g1szSrFFpCQfvbTrLFBOXxtskWyuXGPUkuFxZgcnk29VUjkwIp80AMHmh63Qd6e0BUcA8jUZiRNdVWD5v0vSPkTdFQZscD61Ollr58rmJ7f3nj7xzzSHpwc9rYoE2EJccDvk1NPJC9yCVaiCpttzQFpzlRy1AIN9qqtkapVyVMSBIzbzicbMsO6T5o0mEs39V8zW6TuPo8YcCT18mmHDsGMfLT1FUai18Hz70c39CuNmRbFkB6vh77tXpnBPUIlb99CiqvVIzF1NA4FSZoMtA1sIl91ou84xGT4AY56O1yBelhlPMwaRYw1MTSULKaeLTvxLZefBhQmWagTw4QtOXbm4GdN859jxeATaZ3RK6bOFcB0SlyhQW6egmC0UxyJPoz5Cm0GUogp087fzHsAcy8udNodOXzJik9J9TLjaw809M2evQXPlAetBUeiAmvHSk1z5Wzn2wP3DFevdkSNfXlnYOe75iqYyqUKsn9K3S2eaLEn1OpIZwrOQ6KzEMoTmAZtQ8oHzHcJxN6aGdSWBgxkQVMfgBVZQf36f98rza9qsyC80BFyCh3PBHF1PRvxbszuRGzVSxN1UpJLkYzTs1i1v4hZzKdovqTxPmjjR5ftJMJc73f69GkxMwjIXofJeb6nZCO34WIMaxxKsLmXkda"
pattern1000 = "UKsn9K3S2eaLEn1OpIZwrOQ6KzEMoTmAZtQ8oHzHcJxN"


# for importing the algorithms
timeitSetup = """
import horspool
import kmp
import rabinkarp
"""


# Run test cases 10 times each. Take the average execution time, convert to milliseconds
# Test Length 10
elapsed = timeit.timeit("kmp.KMPSearch(pattern10, text10)", setup=timeitSetup, globals=globals(), number=10)
elapsed = elapsed/10 * 1000 # multiply by 1000 to convert to milliseconds
print("KMP 10: \t" + str(elapsed))

elapsed = timeit.timeit("rabinkarp.RabinKarpSearch(pattern10, text10)", setup=timeitSetup, globals=globals(), number=10)
elapsed = elapsed/10 * 1000 # multiply by 1000 to convert to milliseconds
print("RabinKarp 10: \t" + str(elapsed))

elapsed = timeit.timeit("horspool.HorspoolSearch(pattern10, text10)", setup=timeitSetup, globals=globals(), number=10)
elapsed = elapsed/10 * 1000 # multiply by 1000 to convert to milliseconds
print("Horspool 10: \t" + str(elapsed) + "\n")


# Test Length 100
elapsed = timeit.timeit("kmp.KMPSearch(pattern100, text100)", setup=timeitSetup, globals=globals(), number=10)
elapsed = elapsed/10 * 1000 # multiply by 1000 to convert to milliseconds
print("KMP 100: \t" + str(elapsed))

elapsed = timeit.timeit("rabinkarp.RabinKarpSearch(pattern100, text100)", setup=timeitSetup, globals=globals(), number=10)
elapsed = elapsed/10 * 1000 # multiply by 1000 to convert to milliseconds
print("RabinKarp 100: \t" + str(elapsed))

elapsed = timeit.timeit("horspool.HorspoolSearch(pattern100, text100)", setup=timeitSetup, globals=globals(), number=10)
elapsed = elapsed/10 * 1000 # multiply by 1000 to convert to milliseconds
print("Horspool 100: \t" + str(elapsed) + "\n")


# Test Length 200
elapsed = timeit.timeit("kmp.KMPSearch(pattern200, text200)", setup=timeitSetup, globals=globals(), number=10)
elapsed = elapsed/10 * 1000 # multiply by 1000 to convert to milliseconds
print("KMP 200: \t" + str(elapsed))

elapsed = timeit.timeit("rabinkarp.RabinKarpSearch(pattern200, text200)", setup=timeitSetup, globals=globals(), number=10)
elapsed = elapsed/10 * 1000 # multiply by 1000 to convert to milliseconds
print("RabinKarp 200: \t" + str(elapsed))

elapsed = timeit.timeit("horspool.HorspoolSearch(pattern200, text200)", setup=timeitSetup, globals=globals(), number=10)
elapsed = elapsed/10 * 1000 # multiply by 1000 to convert to milliseconds
print("Horspool 200: \t" + str(elapsed) + "\n")


# Test Length 300
elapsed = timeit.timeit("kmp.KMPSearch(pattern300, text300)", setup=timeitSetup, globals=globals(), number=10)
elapsed = elapsed/10 * 1000 # multiply by 1000 to convert to milliseconds
print("KMP 300: \t" + str(elapsed))

elapsed = timeit.timeit("rabinkarp.RabinKarpSearch(pattern300, text300)", setup=timeitSetup, globals=globals(), number=10)
elapsed = elapsed/10 * 1000 # multiply by 1000 to convert to milliseconds
print("RabinKarp 300: \t" + str(elapsed))

elapsed = timeit.timeit("horspool.HorspoolSearch(pattern300, text300)", setup=timeitSetup, globals=globals(), number=10)
elapsed = elapsed/10 * 1000 # multiply by 1000 to convert to milliseconds
print("Horspool 300: \t" + str(elapsed) + "\n")


# Test Length 400
elapsed = timeit.timeit("kmp.KMPSearch(pattern400, text400)", setup=timeitSetup, globals=globals(), number=10)
elapsed = elapsed/10 * 1000 # multiply by 1000 to convert to milliseconds
print("KMP 400: \t" + str(elapsed))

elapsed = timeit.timeit("rabinkarp.RabinKarpSearch(pattern400, text400)", setup=timeitSetup, globals=globals(), number=10)
elapsed = elapsed/10 * 1000 # multiply by 1000 to convert to milliseconds
print("RabinKarp 400: \t" + str(elapsed))

elapsed = timeit.timeit("horspool.HorspoolSearch(pattern400, text400)", setup=timeitSetup, globals=globals(), number=10)
elapsed = elapsed/10 * 1000 # multiply by 1000 to convert to milliseconds
print("Horspool 400: \t" + str(elapsed) + "\n")


# Test Length 500
elapsed = timeit.timeit("kmp.KMPSearch(pattern500, text500)", setup=timeitSetup, globals=globals(), number=10)
elapsed = elapsed/10 * 1000 # multiply by 1000 to convert to milliseconds
print("KMP 500: \t" + str(elapsed))

elapsed = timeit.timeit("rabinkarp.RabinKarpSearch(pattern500, text500)", setup=timeitSetup, globals=globals(), number=10)
elapsed = elapsed/10 * 1000 # multiply by 1000 to convert to milliseconds
print("RabinKarp 500: \t" + str(elapsed))

elapsed = timeit.timeit("horspool.HorspoolSearch(pattern500, text500)", setup=timeitSetup, globals=globals(), number=10)
elapsed = elapsed/10 * 1000 # multiply by 1000 to convert to milliseconds
print("Horspool 500: \t" + str(elapsed) + "\n")


# Test Length 600
elapsed = timeit.timeit("kmp.KMPSearch(pattern600, text600)", setup=timeitSetup, globals=globals(), number=10)
elapsed = elapsed/10 * 1000 # multiply by 1000 to convert to milliseconds
print("KMP 600: \t" + str(elapsed))

elapsed = timeit.timeit("rabinkarp.RabinKarpSearch(pattern600, text600)", setup=timeitSetup, globals=globals(), number=10)
elapsed = elapsed/10 * 1000 # multiply by 1000 to convert to milliseconds
print("RabinKarp 600: \t" + str(elapsed))

elapsed = timeit.timeit("horspool.HorspoolSearch(pattern600, text600)", setup=timeitSetup, globals=globals(), number=10)
elapsed = elapsed/10 * 1000 # multiply by 1000 to convert to milliseconds
print("Horspool 600: \t" + str(elapsed) + "\n")


# Test Length 700
elapsed = timeit.timeit("kmp.KMPSearch(pattern700, text700)", setup=timeitSetup, globals=globals(), number=10)
elapsed = elapsed/10 * 1000 # multiply by 1000 to convert to milliseconds
print("KMP 700: \t" + str(elapsed))


elapsed = timeit.timeit("rabinkarp.RabinKarpSearch(pattern700, text700)", setup=timeitSetup, globals=globals(), number=10)
elapsed = elapsed/10 * 1000 # multiply by 1000 to convert to milliseconds
print("RabinKarp 700: \t" + str(elapsed))

elapsed = timeit.timeit("horspool.HorspoolSearch(pattern700, text700)", setup=timeitSetup, globals=globals(), number=10)
elapsed = elapsed/10 * 1000 # multiply by 1000 to convert to milliseconds
print("Horspool 700: \t" + str(elapsed) + "\n")


# Test Length 800
elapsed = timeit.timeit("kmp.KMPSearch(pattern800, text800)", setup=timeitSetup, globals=globals(), number=10)
elapsed = elapsed/10 * 1000 # multiply by 1000 to convert to milliseconds
print("KMP 800: \t" + str(elapsed))

elapsed = timeit.timeit("rabinkarp.RabinKarpSearch(pattern800, text800)", setup=timeitSetup, globals=globals(), number=10)
elapsed = elapsed/10 * 1000 # multiply by 1000 to convert to milliseconds
print("RabinKarp 800: \t" + str(elapsed))

elapsed = timeit.timeit("horspool.HorspoolSearch(pattern800, text800)", setup=timeitSetup, globals=globals(), number=10)
elapsed = elapsed/10 * 1000 # multiply by 1000 to convert to milliseconds
print("Horspool 800: \t" + str(elapsed) + "\n")


# Test Length 900
elapsed = timeit.timeit("kmp.KMPSearch(pattern900, text900)", setup=timeitSetup, globals=globals(), number=10)
elapsed = elapsed/10 * 1000 # multiply by 1000 to convert to milliseconds
print("KMP 900: \t" + str(elapsed))

elapsed = timeit.timeit("rabinkarp.RabinKarpSearch(pattern900, text900)", setup=timeitSetup, globals=globals(), number=10)
elapsed = elapsed/10 * 1000 # multiply by 1000 to convert to milliseconds
print("RabinKarp 900: \t" + str(elapsed))

elapsed = timeit.timeit("horspool.HorspoolSearch(pattern900, text900)", setup=timeitSetup, globals=globals(), number=10)
elapsed = elapsed/10 * 1000 # multiply by 1000 to convert to milliseconds
print("Horspool 900: \t" + str(elapsed) + "\n")


# Test Length 1000
elapsed = timeit.timeit("kmp.KMPSearch(pattern1000, text1000)", setup=timeitSetup, globals=globals(), number=10)
elapsed = elapsed/10 * 1000 # multiply by 1000 to convert to milliseconds
print("KMP 1000: \t" + str(elapsed))

elapsed = timeit.timeit("rabinkarp.RabinKarpSearch(pattern1000, text1000)", setup=timeitSetup, globals=globals(), number=10)
elapsed = elapsed/10 * 1000 # multiply by 1000 to convert to milliseconds
print("RabinKarp 1000: \t" + str(elapsed))

elapsed = timeit.timeit("horspool.HorspoolSearch(pattern1000, text1000)", setup=timeitSetup, globals=globals(), number=10)
elapsed = elapsed/10 * 1000 # multiply by 1000 to convert to milliseconds
print("Horspool 1000: \t" + str(elapsed) + "\n")
