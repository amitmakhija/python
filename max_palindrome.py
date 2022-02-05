'''
This function finds out the maximum length of the palindrome within a string
'''

lst = ["114112724353","12342778772376","215342156"]

def check_palindrome(s):

    max_len = 0
    
    def check_naxlen(p1,p2):
        
        while p1 >= 0 and p2 < len(s):
            if s[p1] == s[p2]:
                p1-=1
                p2+=1
            else:
                break
         
        return p2-p1-1

    for i in range(len(s)-1):
        max_len = max(max_len, check_naxlen(i, i+1))
        max_len = max(max_len, check_naxlen(i-1, i+1))

    return max_len

for i in lst:
    i = list(i)
    print(check_palindrome(i))