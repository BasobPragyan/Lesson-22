def palindrome(t):
    e=len(t)-1
    s=0
    while(s<e):
        if(t[s]!=t[e]):
            return False
        s+=1
        e-=1
    return True
tup=(1,2,3,3,2,1)
if palindrome(tup):
    print(tup,"is a palindrome")
else:
    print(tup,"is not a palindrome")