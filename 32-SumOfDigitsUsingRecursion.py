'''
TWO METHODS TO GET SUM OF DIGITS

'''

def SumRecursion(n):
    if n<10:
        return n
    else:
        return SumRecursion(n//10)+n%10
    

result=SumRecursion(12345)
print(result)

'''
SIMPLE FUNCTION TO FIND SUM OF DIGITS
'''
def SumSimple(n):
    sum=0
    while(n>0):
        last_digits=n%10
        sum=sum+last_digits
        n=n//10
    return sum

result1=SumSimple(12345)
print(result1)