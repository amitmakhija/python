'''
This program takes the list of numbers and finds the HCF of all the those numbers
'''


def main(a,b):
    if a == 0:
        return b
    else:
        return main(b%a,a)

if __name__ == '__main__':
    import sys
    sys.setrecursionlimit(150000)
    N = list(map(int,list(input("Enter two numbers separated by space : ").split())))
    a = main(N[0],N[1])
    for i in range(len(N)-2):
        a = main(a,N[i+2])
        
    print(a)