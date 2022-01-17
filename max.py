'''
This program finds out the maximum integer from the list of integers
'''

def max(lst):
    max = 0
    for i in range(len(lst)):
        if lst[i]>max:
            max = lst[i]
    return max
            
lst = list(map(int,input("Enter a list of integers separated by spaces : ").split()))
print(max(lst))