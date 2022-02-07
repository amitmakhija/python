'''
Write a function that takes two lists. list1 contains 0s and 1s. 
0 means i win and 1 means opposite person wins.
list2 contains the amount of bets.
Now i have the power to reverse the winner of one more more "Consecutive" bets from beginning to end
I can use this power only once.
Say if i reverse 1st and 4th bet i also have to reverse 2nd and 3rd bet in between
I can only reverse consecutive bets. No. of bets can be 1 till N
I have to find the maximum possible amount that i can win

eg : a = [0,0,0,0,1] and b = [20,10,60,3,2]
The maximum i can win is by flipping the winner of last bet and the total amount won would be 95

a = [1,0,0,0,1] and b =[20,40,1,1,10]
The maximum i can win here is by only flipping the winner of first bet and the total amount won would be 62
If i flip first and last both, i need to flip the bets in between also.
'''

a = [([1,0,1,0,1,1,1,0],[20,40,10,15,4,2,67,80]),
([1,0,0,0,1],[20,40,1,1,10]),
([0,0,0,0,1], [20,10,60,3,2])]

def maxSubArray(a):
     
    max_so_far =a[0]
    curr_max = a[0]
    st = 0
    en = 0
    st_o = 0
     
    for i in range(0,len(a)):
        curr_max = curr_max + a[i]
        if curr_max < 0:
            st = i+1
            curr_max = 0
        elif curr_max > max_so_far:
            en = i
            max_so_far = curr_max
            st_o = st
        
    return st_o,en

def solve(a,b):
    sum = 0
    b1 = []
    for i in range(len(a)):
        if a[i] == 0:
            b1.append(-b[i])
        else:
            b1.append(b[i])
    
    st,en =  maxSubArray(b1)
    for i in range(len(b)):
        if i in range(st,en + 1):
            if a[i] == 1:
                sum += b[i]
            else:
                sum -= b[i]
        else:
            if a[i] == 0:
                sum += b[i]
    
    return sum

for i in a:
    print(solve(i[0], i[1]))

