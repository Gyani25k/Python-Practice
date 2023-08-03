'''
METHOD 1

'''

def arrayshiftdelete(l,idx):
    l.pop(idx)
    l.append(0)
    return l


'''
METHOD 2

'''

def arrayshiftdelete1(l,idx):
    temp=l[idx]
    n=len(l)
    for i in range (idx,len(l)-1):
        l[i]=l[i+1]

    l[n-1]=0

    return l


l=[1,2,3,4]
idx=2
result=arrayshiftdelete1(l,idx)
result1=arrayshiftdelete(l,idx)
print(result)
print(result1)
    