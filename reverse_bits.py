'''
Problem Description
Reverse the bits of an 32 bit unsigned integer A.
This function takes a number, finds binary of that number, 
stores the binary in 32 bits with extra zeros in the front
Reverses the binary and then returns the integer value.
'''


def reverse_bit(n):
    import math
    s =int(format(n,"b")[::-1],2)
    k = math.floor((math.log2(n)))+1
    print(s<<(32-k))
    
n = int(input("Enter a number : "))

reverse_bit(n)