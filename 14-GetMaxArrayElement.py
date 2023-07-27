# Method 1 Using List Inbuilt Functions (max())

list1=[2,4,78,32,12,5,3,7]
print(max(list1))

# Method 2 Using For Loop 

for i in list1:
    for j in list1:
        if j>i:
            break
    else:
        print(i)


# Time Complexity of Method 2 is O(n^2)

# Method 3 Most Efficient Method

res = list1[0]
for i in range(1,len(list1)):
    if list1[i]>res:
        res=list1[i]
print(res)

# Time Complexity of Method 3 is O(n)
