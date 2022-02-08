'''
This program finds the number of duplicaate values of any number
'''

lst = [[1,2,33,4,5,4,3,2,3,5,8]]

def solve(lst):
    a = {}
    for i in lst:
        if i not in a:
            a[i] = 1
        else:
            a[i] += 1
    
    return a

for i in lst:
    print(solve(i))