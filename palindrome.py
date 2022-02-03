''' This function takes the list of list of numbers and checks if the numbers are palindrome
Returns True for each list checked 
'''
def check_palindrome_int(arr1):
    
    if len(arr1)%2 == 0:
        mid1 = int(len(arr1)/2)
        mid2 = int(len(arr1)/2)+1
    else :
        mid1 = int(len(arr1)/2)
        mid2 = int(len(arr1)/2)+2
        
    pal = True
    for i in range(mid1):
        if arr1[mid1-i-1] != arr1[mid2+i-1]:
            pal = False
    
    return pal

#usecases
arr = []
arr.append([1,2,3,4,5,6,5,4,3,2,1])
arr.append([1,2,3,2,1])
arr.append([1,2,3,3,2,1])
arr.append([1,2,3,3,1,1])

for i in arr:
    print(check_palindrome_int(i))

