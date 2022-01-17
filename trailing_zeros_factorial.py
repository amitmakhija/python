'''
The program gives the no. of trailing zeros in any factorial
No. of trailing zeros are no. of fives(5s) present in the factorial
Hence we count the no. of fives present and then that is the answer
'''

def fact(n):
    fact = 1
    for i in range(n):
        fact = fact * (i+1)
    return fact

def no_of_fives(n):
    n = fact(n)
    count = 0
    while (n % 5)==0:
        count+=1
        n = n//5
    return count

n = int(input("Enter a number : "))
print("Factorial = ",fact(n))
print("No of zeros : ",no_of_fives(n))