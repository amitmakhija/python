
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
                B = B[j+1:]         # Cuts the previous part of  B string
                break               # Cuts the further search in B
    
    if len(lst) == len(A):
        return "YES"
    else:
        return "NO"


def solve(A, B):
        D={}
        ans=[]
        temp1=0
        if A in B:
            return "YES"
        elif len(A)>len(B):
            return "NO"
        for i in range(len(A)):
            a=A[i]
            if A[i] in B:
                temp1=B.find(A[i],temp1)
                D[a]=temp1
                ans.append(temp1)
        
        for i in range(1,len(ans)):
            if ans[i]<ans[i-1]:
                return "NO"
        return "YES"


print(solve(A, B))