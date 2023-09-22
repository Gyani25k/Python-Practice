
# METHOD 1 WITH TIME COMPLEXITY (M+N)LOG(M+N)

def mergetwo(a,b):
    res=a+b
    res.sort()
    return res

a=[10,15]
b=[5,6,6,7,30,40]

result=mergetwo(a,b)
print(result)