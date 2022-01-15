def main(bal,itr):
    for i in range(itr):
        j = list(map(int,list(input("Enter the operation and amount : ").split())))
        if j[0]==1:
            bal = bal + j[1]
        elif j[0] == 2:
            if bal >= j[1]:
                bal = bal - j[1]
            else:
                print("Insufficient funds")
        print("Balance = ",bal)

if __name__ == '__main__':
    bal=int(input())
    itr=int(input())  
    main(bal,itr)