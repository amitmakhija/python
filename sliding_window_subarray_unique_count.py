'''
Given an array of size N, we have to find the unique elements
in a subarray of size K
'''


A = [1, 2, 1, 3, 4, 3]
B = 3

def solve(A,B):
    ans = []
    freq_dict = dict()
    for i in range(B):
        if A[i] not in freq_dict:
            freq_dict[A[i]] = 1
        else:
            freq_dict[A[i]] += 1
    ans.append(len(freq_dict))
    for i in range(B,len(A)):
        freq_dict[A[i-B]] -=1
        if freq_dict[A[i-B]] == 0:
            del(freq_dict[A[i-B]])
        
        if A[i] not in freq_dict:
            freq_dict[A[i]] = 1
        else:
            freq_dict[A[i]] += 1
        
        ans.append(len(freq_dict))

    
    return ans

print(solve(A,B))