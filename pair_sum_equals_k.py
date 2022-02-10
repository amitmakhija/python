'''
Given n array elements, check if there exists a pair(i,j)
such that, A[i]+A[j] == k. And i != j
ie sum of any two pairs of the elements is equal to k
eg
A = [2,7,11,13] and k = 18, ans is True A(1,2) gives total as 18 (7+11)
suppose k = 17, ans = False. No such pair exists whose sum is 17 
'''

lst = [8,9,1,-2,4,5,11,-6,7,5]
k = 100

def solve(lst,k):
    freq_dict = dict()

    for i in lst:
        if i not in freq_dict:
            freq_dict[i] = 1
        else:
            freq_dict[i] += 1
    
    for i in lst:
        if i == (k-i) and freq_dict[i] > 1:
            return True
        elif i != (k-i) and (k-i) in freq_dict:
            return True
    
    return False

print(solve(lst,k))