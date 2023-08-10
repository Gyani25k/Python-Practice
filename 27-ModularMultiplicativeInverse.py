'''
Given two integers ‘a’ and ‘m’. 
The task is to find the smallest modular multiplicative inverse of ‘a’ under modulo ‘m’. 
if it does not exist then return -1.
'''
def modInverse(a,m):
    for i in range (1,m+1):
        if (a*i)%m==1:
            return i
    return - 1

result=modInverse(3,11)
print(result)
