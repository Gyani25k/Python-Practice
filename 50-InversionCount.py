
class Solution:
    def inversionCount(self, arr, n):
        inv=0
        i=0
        while i<n:
            j=i+1
            while j<n:
                if arr[i]>arr[j]:
                    inv+=1
                j+=1
            i+=1
            
        return inv