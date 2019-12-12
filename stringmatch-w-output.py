import horspool
import kmp
import rabinkarp
import boyermoore

# Length 10
text10 = "XxfRnW7yPQ"
pattern10 = "fRnW"

# Length 100
text100 = "AnL2a8U9dPdmXFDxxqtiL0304mRSFEBlgM3RBiCyHvKv1JyEJyv4JCTC4ExrlSX12f2y6BOtCfluWiGCWuzA5GSZQWSDzhBKy7HX"
pattern100 = "uWiGCWuzA5"

text1000 = "pAgNvne12qXEQElC2fQg3ha8hOEevwIfGGrZAIjbSHQOARzliV12tg3O67PxuWX3AyvDOTV5lhZIlnC1MvsrrP3hqsiltWMFmkoOqXEl9qCBeGgJLqO74G7nMZh89pXV4XLqqoME6BECPHcM9mDsEu5myN6UCUbkPczpSf2dzM5tIEigngi2iI10weOTN67IZMVzTYhEe2wPpIrqCr5NXOXxGpxRoIfJZdnmHi1I1d680IIsmpAMPNppzSaat9VYKeHvyihSCv9Nt6C0uItebky0CTfcZYXRd13DbWb2Y469dPmYeuMFyKxgLCcQpsvPGrP9a0ayiCqmgXmUj6g1szSrFFpCQfvbTrLFBOXxtskWyuXGPUkuFxZgcnk29VUjkwIp80AMHmh63Qd6e0BUcA8jUZiRNdVWD5v0vSPkTdFQZscD61Ollr58rmJ7f3nj7xzzSHpwc9rYoE2EJccDvk1NPJC9yCVaiCpttzQFpzlRy1AIN9qqtkapVyVMSBIzbzicbMsO6T5o0mEs39V8zW6TuPo8YcCT18mmHDsGMfLT1FUai18Hz70c39CuNmRbFkB6vh77tXpnBPUIlb99CiqvVIzF1NA4FSZoMtA1sIl91ou84xGT4AY56O1yBelhlPMwaRYw1MTSULKaeLTvxLZefBhQmWagTw4QtOXbm4GdN859jxeATaZ3RK6bOFcB0SlyhQW6egmC0UxyJPoz5Cm0GUogp087fzHsAcy8udNodOXzJik9J9TLjaw809M2evQXPlAetBUeiAmvHSk1z5Wzn2wP3DFevdkSNfXlnYOe75iqYyqUKsn9K3S2eaLEn1OpIZwrOQ6KzEMoTmAZtQ8oHzHcJxN6aGdSWBgxkQVMfgBVZQf36f98rza9qsyC80BFyCh3PBHF1PRvxbszuRGzVSxN1UpJLkYzTs1i1v4hZzKdovqTxPmjjR5ftJMJc73f69GkxMwjIXofJeb6nZCO34WIMaxxKsLmXkda"
pattern1000 = "UKsn9K3S2eaLEn1OpIZwrOQ6KzEMoTmAZtQ8oHzHcJxN"

print("Testing 10 character string...")
kmp.KMPSearch(pattern10, text10)
rabinkarp.RabinKarpSearch(pattern10, text10)
boyermoore.BoyerMooreSearch(pattern10, text10)
print("\n")

print("Testing 100 character string...")
kmp.KMPSearch(pattern100, text100)
rabinkarp.RabinKarpSearch(pattern100, text100)
boyermoore.BoyerMooreSearch(pattern100, text100)
print("\n")

print("Testing 1000 character string...")
kmp.KMPSearch(pattern1000, text1000)
rabinkarp.RabinKarpSearch(pattern1000, text1000)
boyermoore.BoyerMooreSearch(pattern1000, text1000)
