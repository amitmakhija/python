'''
Shaggy has an array A consisting of N elements. We call a pair of distinct indices in that array 
as a special pair if elements at that index in the array are equal.

Shaggy wants you to find a special pair such that distance between that pair is minimum. 
Distance between two indices is defined as |i-j|. If there is no special pair in the array then return -1.
'''

def distance(lst):
    dist = []
    for i in range(len(lst)):
        for j in range(i,len(lst)-1):
            if lst[i] == lst[j+1]:
                dist.append(j+1-i)
    if len(dist)==0:
        return -1
    dist.sort()
    return dist[0]
                

lst = [1,2,3,4,5]
print(distance(lst))