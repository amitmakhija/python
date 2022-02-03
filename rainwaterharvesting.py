'''
There a city with buildings of different heights in a row starting... 
and there is a rainfall.. how much water can be stored above the buildings 

eg
if there are only three buildings in a city of heights 5,3,6.
Then no water can be stored above corner buildings of height 5 and 6 as the water will flow  to their left and right.
Max water that can be stored above middle building of height 3 is upto height 5 ie 2 (5 - 3 which is the height of the middle building)
so the answer is 2

in the same way if we are given a list of building heights as [5,4,3,5]
max water that will be store is 3 (1+2 which is above 4 and 3)
'''

def waterlog(arr):
    max_left = 0
    max_right = []
    water = 0
    
    #prepare an array of maximum hight from the right
    for i in range(len(arr)):
        max_right.append(max(arr[-(i+1):]))
    
    # compares the max left and max right and finds max height until which the water can log
    # total amount of water = max height of water log - height of building
    for i in range(len(arr)):
        if i == 0 or i == len(arr)-1:
            continue
        else:
            if arr[i-1]>max_left:
                max_left = arr[i-1]
            m = min(max_left,max_right[-(i+1)]) # m is the max height until which the water can go
            if m > arr[i]:
                water = water + (m - arr[i])
            else :
                pass
    return water

arr = [5,3,6,7,2,3,7,3]
print(waterlog(arr))