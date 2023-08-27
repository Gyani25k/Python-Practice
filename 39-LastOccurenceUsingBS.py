
# METHOD 1 NAIVE METHOD

def lastoccurence1(arr,n,k):
    for i in reversed(range(len(arr))):
        if arr[i]==k:
            return i
    return -1 

arr = [5, 10, 10, 10, 20, 20, 20]
n = 7
k = 21
res1 = lastoccurence1(arr, n, k)
print(res1)





# EFFICIENT METHOD


def lastoccurence(arr, n, k):
    low = 0
    high = n - 1
    while (low <= high):
        mid = (low + high) // 2
        if arr[mid] < k:
            low = mid + 1
        elif arr[mid] > k:
            high = mid - 1
        else:
            if mid == n - 1 or arr[mid] != arr[mid + 1]:
                return mid
            else:
                low = mid + 1


arr = [5, 10, 10, 10, 20, 20, 20]
n = 7
k = 20
res = lastoccurence(arr, n, k)
print(res)