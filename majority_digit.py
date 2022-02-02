'''
This program takes a list and finds out the element with majority times appearance.
Majority = greater than total length / 2
'''

lst = [[1,2,2,2,2,4,5,2,2,2,3,4,1],[5,5,5,3,2,2,2,5,5],[5,4,3,2,3,2,4,5,6]]

def solve(lst):
    majority = lst[0]
    count = 1
    for i in range(len(lst)-1):
        if lst[i] == majority:
            count+=1
        elif count == 0:
            majority = lst[i]
        else:
            count -= 1
    
    count = 0
    for i in lst:
        if i == majority:
            count+=1
    
    if count > (len(lst)//2):
        return majority
    else:
        return "No majority element"

for i in lst:
    print("Total elements = ",len(i),"Majority : ",solve(i))



