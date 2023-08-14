
def numberOfEmployeesWhoMetTarget(hours, target):
    count=0
    for i in hours:
        if i>=target:
            count+=1
    return count

hours=[1,2,3,4,5,6]
target=4
res=numberOfEmployeesWhoMetTarget(hours, target)
print(res)

