'''
This program finds out the maximum integer from the list of integers
'''

def min_max(lst):
    max = lst[0]
    min = lst[0]
    for i in range(len(lst)-1):
        if lst[i+1]>max:
            max = lst[i+1]
    for i in range(len(lst)-1):
        if lst[i+1]<min:
            min = lst[i+1]
    return min, max
            
lst = list(map(int,input("Enter a list of integers separated by spaces : ").split()))
print(min_max(lst))