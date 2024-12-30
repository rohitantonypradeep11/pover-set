import math
def abc(a,size):
    power = int(math.pow(2,size))
    f = 0
    l = 0
    for f in range(0,power):
        for l in range(0,size):
            if f&(1<<l)>0:
                print(a[l], end = "")
s = int(input("enter a size"))
a = []
for i in range(0,s):
    n = int(input("enter a number"))
    a.append(n)
abc(a,len(a))