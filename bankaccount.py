''' Program has function which takes two arguments :
1) initial balanace and 2) No. of operations that you want to perform. which are deposit or withdraw
This function adds the deposit amount to balance and deducts the withdrawal amount from balance
'''


def main(bal,itr):
    for i in range(itr):
        j = list(map(int,list(input("Enter the operation and amount (1 for deposit and 2 for withdrawal) : ").split())))
        if j[0]==1:
            bal = bal + j[1]
        elif j[0] == 2:
            if bal >= j[1]:
                bal = bal - j[1]
            else:
                print("Insufficient funds")
        print("Balance = ",bal)

if __name__ == '__main__':
    bal=int(input("Enter the initial balance : "))
    itr=int(input("Enter the no. of operations you want to perform"))  
    main(bal,itr)