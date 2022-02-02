'''
This program takes an integer as input and finds the nearest lowest 2 raise to power number
'''
def solve(n):
    i=0
    while n > 1:
        n = n>>1
        i+=1
    return 2**i

n = int(input("Enter a number : "))
print(solve(n))
