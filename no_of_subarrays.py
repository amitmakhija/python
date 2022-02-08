'''
Find the no. of substrings starting with 'a' and ending with 'g'
'''

s = "abcgasgkgsgag"

def solve(s):
    ans = 0
    c = 0
    s = list(s)
    for i in range(len(s)-1, -1, -1):
        if s[i] == 'g':
            c += 1
        elif s[i] == "a":
            ans += c 
    
    return ans

print(solve(s))
