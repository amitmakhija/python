'''
We have to find the minimum possible subarry containing the minimum
and maximum value of the entire array
'''

lst = [1,5,4,4,0,4,5,2,6,4,4,2,1]

def solve(lst):
    arg_min = min(lst)
    arg_max = max(lst)
    min_i = None
    max_i = None
    ans = len(lst)

    if arg_min == arg_max:
        ans = 1
    else:
        for i in range(len(lst)-1, -1, -1):
            if lst[i] == arg_min:
                min_i = i
            elif lst[i] == arg_max:
                max_i = i

            if min_i is not None and max_i is not None:
                ans = min(ans,abs(min_i-max_i))
    
    return ans

print(solve(lst))
