'''
FIND IMMEDIATE GREATER THAN X

'''

def immediategreater(l,x):
    greater=float('inf')
    for nums in l:
        if nums>x and nums<greater:
            greater=nums
    if greater == float('inf'):
        return -1
    else:
        return greater
    

'''
FIND IMMEDIATE SMALLER THAN X

'''

def immediatesmaller(l,x):
    close=float('-inf')
    for nums in l:
        if nums<x and nums>close:
            close=nums
    if close == float('-inf'):
        return - 1
    else:
        return close
    
l=[1,3,4,7,2,9]
x=4
result=immediategreater(l,x)
result1=immediatesmaller(l,x)

print(result,result1)
