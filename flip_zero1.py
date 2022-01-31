# lst1 = [[1,0,1,1,0,0,0,0,0,1,1,1],
# [1,0,1,1,0,0,0,1,0,1,1,1],
# [0,0,1,1,0,1,1,0,0,1,1,0],
# [1,0,1,1,1,0,1,0,0,1,1,1]]
'''
This program takes a string of binary digits. Converts any one zero to one from the middle of two Ones such that
the count of no. of ones is maximum

### unable to understand the logic... have copied the code.. 
### Requires further learning..
'''


lst1 = ["101100000111","101100010111","001101100110","101110100111"]

def solve(lst):
    l = 0
    zero_count = 0 #keeps count of zeros
    ans = 0
    for i in range(len(lst)):

        if lst[i] == "0": #if lst[i] eq 0; cnt is increased by 1
            zero_count+=1

        #cnt += A[r] == "0"

        if zero_count > 1:
            if lst[l] == "0":
                zero_count -= 1
            l += 1
        ans = max(ans, i - l + 1)

    return min(ans, lst.count('1'))



for i in lst1:
    print(solve(i))