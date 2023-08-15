'''
Property Of logarithm
'''

def log(n):
    if n == 0:
        return 0  
    else:
        temp = 1 + log(n // 2)
        return temp


result=log(4)
print(result)