'''
WRITE A PROGRAM TO FIND QUADRACTIC ROOTS
'''
import math

def quadracticroots(a,b,c):

    d=b**2-4*a*c
    sq=math.sqrt(abs(d))

    if d>0:
        r1=int(((-b)+sq)//2*a)
        r2=int(((-b)-sq)//2*a)
    elif d==0:
        r1=int((-b)//2*a)
        return r1,r1
    else:
        return -1
    if r1>r2:
        return r1,r2
    return r2,r1


result=quadracticroots(1,2,3)
print(result)
        