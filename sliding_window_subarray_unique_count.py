'''
Given an array of size N, we have to find the unique elements
in a subarray of size K
'''


lst = [6,3,7,3,8,6,9]
k = 3

def solve(lst,k):
    ans = []
    freq_dict = dict()
    for i in range(k):
        if lst[i] not in freq_dict:
            freq_dict[lst[i]] = 1
        else:
            freq_dict[lst[i]] += 1
    ans.append(len(freq_dict))
    for i in range(k,len(lst)):
        freq_dict[lst[i-k]] -=1
        if freq_dict[lst[i-k]] == 0:
            del(freq_dict[lst[i-k]])
        
        if lst[i] not in freq_dict:
            freq_dict[lst[i]] = 1
        else:
            freq_dict[lst[i]] += 1
        
        ans.append(len(freq_dict))

    
    return ans

print(solve(lst,k))