'''
Given a string s, find the length of the longest substring without repeating characters.
'''

s = "abacdefabcbb"

def solve(s):
    str_dict = set()
    l = 0
    max_l = 0    
    for i in s:
        if i not in str_dict:
            str_dict.add(i)
            l+=1
        else:
            max_l = max(max_l, l)   

    return max_l

print(solve(s))

