'''Naive Solution'''

def squareroot(x):
    i=0
    while i*i<=x:
        i+=1
    return i-1

x=4
res=squareroot(4)
print(res)


'''Efficient Solution Using Binary Search'''

def squareroot1(x):
    low=1
    high=x
    ans=-1
    if x==0:
        ans=0
    while(low<=high):
        mid=(low+high)//2
        midsq=mid*mid
        if midsq==x:
            return mid
        elif midsq<x:
            low=mid+1
        else:
            high=mid-1
            ans=mid-1
    return ans

x=1011
res1=squareroot1(x)
print(res1)