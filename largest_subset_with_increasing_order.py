'''
Given N array element, find the length of the longest sequence which can be rearranged in an increasing order where each element is one more than the previous element
eg A = [100,4,200,1,3,2]
Length = 4
'''

A = [4,3,2,1]

def solve(lst):
    s = set(lst)
    ans = 0

    for i in s:
        if i-1 not in s:
            current_num = i
            current_streak = 1

            while current_num+1 in s:
                current_num += 1
                current_streak += 1

            ans = max(ans, current_streak)

    return ans


print(solve(A))