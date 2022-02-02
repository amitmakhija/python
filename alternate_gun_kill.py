'''
There are n people standing in a circle in an order 1 to n.
No.1 has a gun, he kills next person (i.e. no. 2) and gives the gun 
to next to next (i.e no.3). All persons do the same until only 1 survives.

Which number survives at the last?
''' 

n = int(input("Enter the number of persons in the circle : "))
# def solve(n):
#     first = 1
#     i = 1
#     while n > 1:
#         if n % 2 == 1:
#             first = first + (2**i)
#         i+=1
#         n = n//2

#     return first

# def nearest_power_of_two(n):
#     while (n&(n-1)) != 0:
#         n = n & n-1
#     return n<<1

def solve(n):
    import math
    if n & ( n-1) == 0:
        return 1
    else:
        a = int(math.log2(n))
        return (n-(2**a))*2+1

print(solve(n))

    