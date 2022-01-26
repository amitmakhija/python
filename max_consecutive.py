'''
This program takes a string from the user and returns the maximum
number of consecutive repeats
'''

def solve(s):
    b = True
    count1 = 1
    count2 = 0
    for i in range(len(s)-1):
        if s[i]==s[i+1]: 
            count1+=1
        else:
            count1=1
    
        if count1>count2:
            count2 = count1
        
    return count2

s = input("Enter the string : ")
print(solve(s))    