'''
This function takes a string and asks for start and end of a substring
of that string. And then reverses that part of the string ie substring.
'''


s = input("Enter the string : ")
s = list(s)
st,en = map(int,input("Enter the start and end number : ").split())
def reverse(s,st,en):
    p1 = st
    p2 = en
    while p1 < p2:
        s[p1],s[p2] = s[p2],s[p1]
        p1+=1
        p2-=1
    return "".join(s)

#print(st,en)
print(reverse(s,st,en))