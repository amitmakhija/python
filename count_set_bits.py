'''
This program takes a number and counts the number of set bits in that number.
This program uses bitwise operators and reduces the Time complexity
'''


n = int(input("Enter any number : "))

print("Binary representation : "+ format(n,'b'))
count = 0
while(n>0):
    n = n & (n-1)
    count+=1
    
print("No. of ones in the binary : ", count)