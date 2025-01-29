

def caesarCipher(s,n):
    s = list(s)
    alpha = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
    rAlpha = {v:k for k,v in alpha.items()}

    upper = False
    for i in range(len(s)):
        if s[i].isupper():
            upper = True
            s[i] = s[i].lower()
        if s[i].isalpha():
            currentVal = alpha[s[i]]
            nexVal = currentVal + n
            while nexVal > 26:
                nexVal = nexVal - 26
            s[i]= rAlpha.get(nexVal)
        if upper is True:
            upper = False
            s[i] = s[i].upper()

    return ''.join(s);





if __name__ == "__main__":
    s = input()
    n = int(input())

    cipher = caesarCipher(s,n)
    print(s)
    print(cipher)