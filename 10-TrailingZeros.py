
# formula used = [n/5]+[n/25]+.............................

def CountTrailingZeros(n):

    result=0
    i=5

    while (i<=n):
        result=result+n//i
        i=i*5 

    print(result)
    return result

CountTrailingZeros(100)

# Time Complexity = O(logn)
