# METHOD 1 
'''
TO ROTATE BY 1 
'''

def rotate1(l):
    l[:]=l[1:]+l[0:1]
    return l

def rotate2(l):
    l.append(l.pop(0))
    return l

def rotate3(l):
    n=len(l)-1
    x=l[0]
    for i in range(1,n):
        l[i-1]=l[i]
    l[n-1]=x
    return l

'''
METHOD 2 ROTATE BY D
'''

def rotate4(l,d):
    l[:]=l[d:0]+l[0:d]
    return d
