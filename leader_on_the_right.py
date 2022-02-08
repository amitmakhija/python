'''
Given an array A of size N, you have to count the no. of leaders in the array
An element is a leader if it is strictly greater than all the elements to its right side.
'''

lst = [15,-1,7,2,5,4,2,3]

def solve(lst) :
    count = 0
    big = 0
    for i in range(len(lst)-1,-1,-1):
        if lst[i] > big :
            big = lst[i]
            count = count + 1
        
    return count

print(solve(lst))