'''
This function takes a word and toggles each character of this word.
Toggle = switching the case of the letter from capital to small or from small to capital
'''

s = input("Enter any word : ")
s = list(s)
toggle_s = []

def toggle(s):
    for i in s:
        i = chr(ord(i) ^ 32)
        toggle_s.append(i)
    return "".join(toggle_s)

print(toggle(s))

