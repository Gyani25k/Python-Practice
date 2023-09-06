'''
In selection sort we first pick the first minimum element put on the first index then second minimum then put on the second place we have 
to repeat this till we get the sorted array

'''



def selectionsort(l):
    n=len(l)
    for i in range(n-1):
        min_index=i
        for j in range(i+1,n):
            if l[j]<l[min_index]:
                min_index=j
            l[min_index],l[i]=l[i],l[min_index]
    return l
            
l=[1,3,2,6,8]
result1=selectionsort(l)
print(result1)