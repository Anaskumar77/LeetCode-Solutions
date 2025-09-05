# s = "(()()()){]"
s = "(((((("

def hello(s):
    s = list(s)
    d = {')':'(',']':'[','}':'{'}
    j = 1

    for i in range(1,len(s)):
        
        if s[0] in d: return False

        elif s[j] in d:

            if s[j-1] == d[s[j]]:
                del s[j-1]
                del s[j-1]
                j -= 1

            else: return False

        else: j += 1

    if len(s) == 0: return True  

print(hello(s))