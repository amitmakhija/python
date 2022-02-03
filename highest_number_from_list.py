'''
This program take a list of integers and sorts them in such an order than if we
combine those elements in that order, we will get the highest number possible.
'''


from functools import cmp_to_key

lst = [3,30,34,5,9]
print(lst)


def solve(lst):
    lst.sort(key=cmp_to_key(my_cmd))
    return lst

def my_cmd(x,y):
    if int(str(x) + str(y)) < int(str(y)+str(x)):
        return 1
    elif int(str(x) + str(y)) > int(str(y)+str(x)):
        return -1
    else :
        return 0


print (solve(lst))