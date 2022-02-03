'''
This program does binary search. It searches the presence of key in the given list. 
And returns the index of the found key in the list
If the element is not found, it returns -1
'''

A = [2,4,7,9,10,2,1,5,3]
A.sort()

def bin_search(lst, key):
    start = 0
    end = len(lst)-1
    found = False
    while start <= end:
        mid = (start+end)//2
        if lst[mid] == key:
            found = True
            break
        elif lst[mid] > key:
            # Search in left half
            end = mid-1
        else:
            # Search in right half
            start = mid+1
    
    if found == True:
        return mid
    else:
        return -1

print(A)
key = int(input("Enter a number : "))
print(bin_search(A, key))