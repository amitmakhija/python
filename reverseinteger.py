'''This program takes an integer and reverses the digits of that integer
'''

def main(n):
    ans = n[::-1]
    print("The no. you entered : ",int(n))
    print("The reverse of the no. is : ",ans)


if __name__ == '__main__':
    n=int(input("Enter the no. of integers you want to reverse : "))
    for i in range(n):
        no=input("Enter an integer : ")
        main(no)
