''' This program takes integer and counts the no. of digits in the integer without converting or slicing a 
string...................
'''

def main(n):
    count = 0
    i = 1
    while n>0:
        n = n//10
        count += 1
        
    return count

if __name__ == '__main__':
    n = int(input("Enter an integer : "))
    print(main(n))
