'''
This function takes a sentence and reverses each word of the sentence.
'''

s = input("Enter a sentence : ")
s = list(s)

def reverse(s,f,l):                         #s = list of chars of the string, f and l are first and last position
    while f < l:
        s[f],s[l] = s[l],s[f]
        f+=1
        l-=1
    return s

def reverse_words(s):
    f = 0
    l = len(s)-1
    s = reverse(s, f, l)                    #Reverse the whole string 
    for i in range(len(s)):
        if s[i] == " " or i == len(s)-1:
            if s[i] == " ":
                l = i-1
                s = reverse(s,f,l)        #reverse back each word
                f = i+1
            else:
                l = i
                s = reverse(s, f, l)
    
    return "".join(s)

print(reverse_words(s))
        

