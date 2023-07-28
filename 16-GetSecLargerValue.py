# METHOD 1

def greter(l):
    if len(l)<=1:
        return None
    res=l[0]
    for i in range(1,len(l)):
        if l[i]>res:
            res=l[i]
    return res

def secondlarger(l):
    if len(l)<=1:
        return None
    lar = greter(l)
    slar = None
    for j in l:
        if j != lar:
            if slar == None:
                slar= j
            else:
                slar=max(j,slar)
    return slar

l=[2,4,5,3]
result1=greter(l)
print(result1)
result2=secondlarger(l)
print(result2)


# METHOD 2 (EFFICIENT METHOD)

def getsecondlarger(l):
    if len(l)<=1:
        return None
    lar=l[0]
    slar = None
    for x in l:
        if x>lar:
            slar=lar
            lar=x
        elif x!= lar:
            if slar==None or slar<x:
                slar=x
    return slar

l=[2,4,5,3]
result3=getsecondlarger(l)
print(result3)