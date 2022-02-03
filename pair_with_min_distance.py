'''
This program takes a list of integers and finds the min distance between any
two pair of the possible pairs of elements.
'''

lst = [-10,9,3,8,10,2,15, -3, -5, 13]
def solve(lst):
    import sys
    if len(lst) < 2:
        return "Atleast two elements required"
    else:
        dist = sys.maxsize
        #print(dist)
        lst = sorted(lst)
        for i in  range(1,len(lst)):
            if lst[i] == lst[i-1]:
                return 0
            else:
                # if dist > abs(lst[i] - lst[i-1]):
                #     dist = abs(lst[i] - lst[i-1])
                dist = min(dist,lst[i]-lst[i-1])

    return dist

print(solve(lst))