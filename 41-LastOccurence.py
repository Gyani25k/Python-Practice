
# METHOD 1 NAIVE METHOD

def lastoccurence(l,x):
    for i in reversed(range(len(l))):
        if l[i]==x:
            return i
    return -1

l=[1,2,2,2,2,2,2]
x=2
res=lastoccurence(l,x)
print(res)


# EFFICIENT METHOD

def lastoccurence1(l,x):
    start=0
    end=len(l)-1
    while start<=end:
        mid=(start+end)//2
        if l[mid]<x:
            start=mid+1
        elif l[mid]>x:
            end=mid-1
        else:
            if mid==len(l)-1 or l[mid]!=l[mid+1]:
                return mid
            else:
                start=mid+1

l=[1,2,2,2,2,2,2]
x=2
res1=lastoccurence1(l,x)
print(res1)
