'''
The program gives the no. of trailing zeros in any factorial
No. of trailing zeros are equal to no. of fives(5s) present in the factorial
Hence we count the no. of fives present and then that is the answer
'''

def no_of_fives(n):
    count = 0
    while n > 0:
        n = n//5
        count += n
    
    return count            
        

n = int(input("Enter a number : "))
print("No of zeros : ",no_of_fives(n))
