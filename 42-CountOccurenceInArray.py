
# LINEAR SEARCH 

def linear(l,k):
    count=0
    for i in range(len(l)):
        if l[i]==k:
            count+=1
    return count

l=[1,2,2,2,2,2,2,2,2,5,4]
k=2
res=linear(l,k)
print(res)


# EFFICIENT METHOD

def firstoccurence(l, k):
    start = 0
    end = len(l) - 1
    while start <= end:
        mid = (start + end) // 2
        if l[mid] < k:
            start = mid + 1
        elif l[mid] > k:
            end = mid - 1
        else:
            if mid == 0 or l[mid] != l[mid + 1]:
                return mid
            else:
                end = mid - 1

    return -1

def lastoccurence(l, k):
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (low + high) // 2
        if l[mid] < k:
            low = mid + 1
        elif l[mid] > k:
            high = mid - 1
        else:
            if mid == len(l) - 1 or l[mid] != l[mid + 1]:
                return mid
            else:
                low = mid + 1

    return -1

def countoccurence(l, k):
    first = firstoccurence(l, k)
    if first == -1:
        return 0
    else:
        return lastoccurence(l, k) - first + 1

l = [1, 2, 2, 2, 2, 2, 2, 2, 2, 4, 5]
k = 2
res1 = countoccurence(l, k)
print(res1)
