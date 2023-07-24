'''Insertion is a basic but frequently used operation. Arrays in most languages cannnot be dynamically shrinked or expanded. 
Here, we will work with such arrays and try to insert an element at some index.
You are given an array arr(0-based index). 
The size of the array is given by sizeOfArray. You need to insert an element at given index.'''

class Solution:
    '''You need to insert the given element at the given index. 
    After inserting the elements at index, elements
    from index onward should be shifted one position ahead
     You may assume that the array already has sizeOfArray - 1
    elements.'''
    
    def insertAtIndex(self, arr, sizeOfArray, index, element):
        #Your code here
        arr.insert(index,element)
        
        return arr