'''
This function takes 2D list and checks if any row
or column has zero in it. If it has it makes that entire row or
column as zero
'''


lst = [[5,8,2,0,3,4,3,4,9,1],
[3,7,2,6,0,1,2,3,4,0],
[5,6,6,7,1,5,2,7,4,7],
[10,2,1,3,5,7,7,9,5,6],
[2,10,10,0,5,5,2,4,4,3]]

def solve(lst):
    import numpy as np
    a = np.array(lst)
    b = a.copy()

    for i in range(a.shape[0]):
        if np.any(a[i]==0):
            b[i]*=0

    for i in range(a.shape[1]):
        if np.any(a.T[i] == 0):
            b.T[i] *= 0

    return b


print(solve(lst))