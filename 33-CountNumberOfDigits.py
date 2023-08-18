'''
COUNT NUMBER OF DIGITS
'''

def CountSimple(n):
    digits=0
    while (n!=0):
        n=n//10
        digits+=1
    return digits

result=CountSimple(123)
print(result)


def countDigit(n):
    if n//10 == 0:
        return 1
    return 1 + countDigit(n // 10)

result1=countDigit(123234)

print(result1)