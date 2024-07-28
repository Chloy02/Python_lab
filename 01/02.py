A = ["abc", "xyz", "aba", "1221"]

for i in range(0, len(A)):
    stri = A[i]
    if stri[0] == stri[-1]:
        print("index: ", A.index(A[i]) , "String: ", stri)

