# METHOD 1

def reverselist(l):
    l.reverse()
    return l

l=[12,23,11]
result=reverselist(l)
print(result)


# METHOD 2

def reverselist1(l):
    new_list= list(reversed(l))
    return new_list


l=[12,23,11]
result1=reverselist1(l)
print(result1)

# METHOD 3

def reverselist2(l):
    new_list=l[::-1]
    return new_list

l=[12,23,11]
result2=reverselist2(l)
print(result2)

# METHOD 4

def reverselist3(l):
    start=0
    end=len(l)-1
    while(start<end):
        l[start],l[end] = l[end],l[start]
        start=start+1
        end=end-1

    return l 

l=[12,23,11]
result3=reverselist3(l)
print(result3)