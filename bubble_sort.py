'''
This function performs the sorting using bubble sort algorithm
'''

lst = [[2,3,4,2,1,5,6],[3,1,6,9,3,2,80]]

def solve(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - 1):
            if lst[j] > lst[j+1]:
                lst[j+1] = lst[j]
    
    return lst

for i in lst:
    print(solve(i))