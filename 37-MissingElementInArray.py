'''
Given an array of size N-1 such that it only contains distinct integers in the range of 1 to N. 
Find the missing element.
'''
# Method 1

def missingvalue(array,n):
    for i in range(1,n+1):
        if i not in array:
            return i

array=[1,2,4,5]
n=5   
result=missingvalue(array,n)
print(result)


'''
ERROR FOR METHOD 1:

Test Cases Passed: 
108 /307
Time Limit Exceeded

Your program took more time than expected.Expected Time Limit : 1.35sec
'''

# Method 2

def missingvalue1(array,n):
    sum_of_array_elements=sum(array)
    sum_of_n_elements=(n*(n+1))/2
    missing_element=int(sum_of_n_elements-sum_of_array_elements)
    return missing_element

array=[1,2,4,5]
n=5   
result1=missingvalue1(array,n)
print(result1)


'''
RESULT:

Problem Solved Successfully

Test Cases Passed: 
307 /307
Total Points Scored: 
2 /2
Your Total Score: 
105
Total Time Taken: 
0.33

'''