'''
REMOVE TRAILING ZEROS FROM INT

'''

def removetrailingint(n):
    while(n%10==0):
        n=n//10
    return n

n=20302000
result=removetrailingint(n)
print(result)


'''
REMOVE TRAILING ZEROS FROM STR

'''

def removetrailingstr(a):
    while(a[-1]=="0"):
        a=a[:-1]
    return a

a="20302000"
result1=removetrailingstr(a)
print(result1)