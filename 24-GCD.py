'''
METHOD 1 EUCLIDIAN

'''

def gcd(a,b):
    while (a!=b):
        if a>b:
            a=b-a
        else:
            b=b-a
    return a


'''
METHOD 2 OPTIMIZED EUCLIDIAN

'''

def gcd1(a,b):
    if b==0:
        return a
    return gcd1(a,a%b)

result=gcd(10,4)
print(result)

result1=gcd1(2,6)
print(result1)