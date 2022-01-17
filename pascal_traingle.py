def factorial(n):
    fact = n
    
    for i in range(n-1):
        fact = fact * (n-(i+1))
    
    return fact

def combination(n,r):
    if n-r < r:
        r = n-r
    
    num =n
    
    for i in range(r-1):
        num = num * (n-(i+1))
    den = factorial(r)
    
    if den == 0:
        return 1 
    else:
        return (num//den)
    
def pascal(n):
    for i in range(n):
        for j in range(n):
            if j<=i:
                print(combination(i, j), end = " ")
            else :
                print("0", end = " ")
        print("")
    
        
if __name__ == '__main__':
    n = int(input("Enter the number n : "))
    pascal(n)
    
    
    