'''
Write a program to input from user five numbers(A, B, C, D & E) representing 
marks of student in 5 subjects out of 100. You have to calculate percentage and 
then Grade of each student.

If percentage >= 90% : Grade A
If percentage >= 80% : Grade B
If percentage >= 70% : Grade C
If percentage >= 60% : Grade D
If percentage >= 40% : Grade E
If percentage < 40% : Grade F
'''


def main(lst):
    count = 0
    lst = list(map(int,list(lst.split())))
    for i in lst:
        count = count + i
    perc = count/len(lst)
    perc1 = perc // 10
    
    switcher = {
    9 : "Grade A",
    8 : "Grade B",
    7 : "Grade C",
    6 : "Grade D",
    5 : "Grade E",
    4 : "Grade E"        
    }
    
    grade = switcher.get(perc1,"Grade F")
    
    return perc, grade

if __name__ == '__main__':
    n = input("Enter the list of integers : ")
    print(main(n))    