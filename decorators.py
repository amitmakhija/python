'''
This program implements decorators. Decorator takes a function, performs some additional activity and returns a function.
This program checks the authorisation and then runs the function
'''



def authorisation(func):
    A = {"Amit":"Tiger99"}
    def inner(*args, **kwargs):
        B = list(input("Enter Username and Password separated by space : ").split())
        if B[0] in A and A[B[0]] == B[1]:
            return func(*args, **kwargs)
        else:
            print("You are not authorized")
    
    return inner

@authorisation
def add(a,b):
    return a+b

print(add(2,4))

        