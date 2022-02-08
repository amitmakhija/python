'''
This program finds the no. of unique values in the list
'''

lst = [[1,2,33,4,5,4,3,2,3,5,8]]

def solve(lst):
    a = set()
    for i in lst:
        a.add(i)
        
    return len(a)


for i in lst:
    print(solve(i))


