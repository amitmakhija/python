a = [2,4,-15,-1,1,3,9,10]

def solve(a):
    c_sum = 0
    max_sum = 0
    st = 0
    en = 0
    st_o = 0
    for i in range(len(a)):
        c_sum += a[i]
        if c_sum < 0:
            c_sum = 0
            st = i+1
        elif c_sum > max_sum:
            max_sum = c_sum
            st_o = st
            en = i
    return max_sum, st, en

print(solve(a))