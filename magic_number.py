'''
This program takes a list of integers and finds number of magic numbers in the list.
A magic number is the number which is equal to the number of elements less than that number in the list.

'''

lst = [[-3,0,2,4,5,5,5,5,8,8,10,10,10,14],[1,1,1,2]]

def solve(lst):
    cnt = 0
    res = 0
    if lst[0] == 0:
        cnt+=1
    for i in range(1,len(lst)):
        if lst[i] != lst[i-1]:
            cnt = i
        if lst[i] == cnt:
            res += 1
    
    return res

for i in lst:
    print(solve(i))