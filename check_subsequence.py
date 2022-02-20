
'''
Given two strings A and B, find if A is a subsequence of B.

Return "YES" if A is a subsequence of B, else return "NO".

'''


A = "bit"
B = "tdfbkjijgbbiihbmmt"

def solve(A, B):
    lst = []
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i] == B[j]:
                lst.append(True)
                B = B[j+1:]
                break
    
    if len(lst) == len(A):
        return "YES"
    else:
        return "NO"

print(solve(A, B))