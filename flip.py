def abc(a,b):
    flip = 0
    while a>0 or b>0:
        t1 = a&1
        t2 = b&1
        if t1 !=t2:
            flip = flip+1
        a>>=1
        b>>=1
    return flip
a = int(input("enter a number"))
b = int(input("enter a number"))
print(abc(a,b))
