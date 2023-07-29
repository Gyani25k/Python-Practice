# METHOD 1

def isSorted(l):
    i=1
    while i< len(l):
        if l[i]<l[i-1]:
            return False
    i+=1
    return True


# METHOD 2

def isSorted1(l):
    sorted_list=sorted(l)
    if sorted_list==l:
        return True
    else:
        return False
    
# METHOD 3

class Solution:
    def findhighestEle(self,arr, n):
        largest = arr[0]
        for i in range(n):
            if (arr[i] > largest):
                largest = arr[i]
        return largest
        
    def isSorted(self,arr,n):
        highest = self.findhighestEle(arr, n)
        i = 1
        while (i < n-1):
            if (arr[0] == highest):
                if (arr[i] < arr[i+1]):
                    return 0
            else:
                if (arr[i] > arr[i+1]):
                    return 0
    
            i = i + 1
        return 1
