def main(a,b):
    def find_hcf(a,b):
        if a == 0:
            return b
        else :
            return (find_hcf(b%a, a))
    
    hcf = find_hcf(a, b)
    return (a*b)//hcf

if __name__ == '__main__':
    import sys
    sys.setrecursionlimit(15000)
    N = list(map(int,input("Enter the list of integers separated by space : ").split()))
    a = main(N[0],N[1])
    for i in range(len(N)-2):
        a = main(a,N[i+2])
    
    print(a)
