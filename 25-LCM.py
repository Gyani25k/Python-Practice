'''
METHOD 1

'''

def lcm(a,b):
    res=max(a,b)
    while True:
        if res%a==0 and res%b==0:
            return res
        else:
            res = res+1
    return res

print(lcm(2,4))

'''
METHOD 2 USING GCD
'''

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
    

def lcm1(a,b):
    return (a*b) //gcd(a,b)