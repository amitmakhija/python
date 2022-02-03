'''
This program perform bubble sort on the list.
It sorts the list in place.....
'''


A = [3,5,1,2,8,9,4,10,2,3]

print(A)
for i in range(len(A)-1):
    for j in range(len(A)-i-1):
        if A[j] > A[j+1]:
            A[j],A[j+1] = A[j+1],A[j]

print(A)