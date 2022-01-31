'''
This program takes a list and rotates the list clockwise by k times.
It uses modular operation
'''


lst = list(map(int,input("Enter the list you want to rotate : ").split()))
k = int(input("Enter the number you want to rotate the list clockwise : "))

def rotate_list(lst,k):
    print("Initial list : ",lst)
    r_list = []
    n = len(lst)
    for i in range(len(lst)):
        r_list.append(lst[(i+k)%n])
    print("Rotated list : ", r_list)
    
rotate_list(lst, k)        