'''
This function takes a list of integers and sorts the list as per the
number of factors of that element.
It uses comparator operator present in sort or sorted function in the form of key
'''

from functools import cmp_to_key

def find_factors(n):
    count = 0
    for i in range(1,n+1):
        if n % i == 0:
            count+=1
            #print(i)
    return count

#print(find_factors(i))
def comparator(x,y):
    if find_factors(x) < find_factors(y):
        return -1
    elif find_factors(x) > find_factors(y):
        return 1
    else:
        return 0

lst = [2,4,6,3,8,36,49,60,128,25]

lst.sort(key  = cmp_to_key(comparator))

print(lst)