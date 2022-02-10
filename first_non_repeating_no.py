'''
Program to find first non repeating element
'''

lst = [2,3,6,2,3,7,5]

def solve(lst):
    a = {}
    for i in lst:
        if i not in a:
            a[i] = 1
        else:
            a[i] += 1
    
    for i in lst:
        if a[i] == 1:
            return i

print(solve(lst))