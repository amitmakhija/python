'''
Given an array, arr[] of size N, the task is to find the count of array indices 
such that removing an element from these indices makes the sum of even-indexed 
and odd-indexed array elements equal.
'''

a=[[2, 1, 6, 4], [1,1,1], [3,5,4,9,5], [1,5,4,9,8,6,8,2,-2], [ 1, 2, 3, 7, 1, 2, 3 ]]

def solve(lst):
    lst1 = []
    l_sum = []
    r_sum = []
    tem = 0

    for i in range(len(lst)):
        if i % 2 == 0:
            lst1.append(lst[i])
        else:
            lst1.append(-lst[i])
    
    for i in range(len(lst1)):
        tem += lst1[i]
        l_sum.append(tem)
    
    tem = 0
    for i in range(len(lst1)-1,-1,-1):
        tem +=  lst1[i]
        r_sum.append(tem)
    
    r_sum.reverse()

    count = 0

    for i in range(len(lst)):
        if l_sum[i] == r_sum[i]:
            #print(i, end=" ")
            count += 1
    
    return count

for i in a:
    print(solve(i))


