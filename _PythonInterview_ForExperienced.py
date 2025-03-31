# -*- coding: utf-8 -*-
"""
Github Link: https://github.com/Tanu-N-Prabhu/Python/blob/master/Python%20Coding%20Interview%20Prep/35%20Python%20interview%20questions%20for%20experienced.md
"""

# What is Type Hinting
# LRU 
# Find the nth Largest number in array(list)
# Find the Longest substring
#


# Answers 

"""
numpy.array is more flexible than a Python list because it is optimized for numerical computations and offers several key advantages:

1. Efficiency & Performance
Memory Efficiency: numpy.array is stored in a contiguous memory block, while Python lists store references to objects, leading to higher memory overhead.

Faster Computation: NumPy operations are implemented in C, making them significantly faster than looping over lists in Python.

2. Vectorized Operations
NumPy supports element-wise operations directly, avoiding the need for explicit loops:
    
3. Broadcasting
NumPy allows arithmetic operations between arrays of different shapes without explicit looping: 
    
    4. Support for Multi-Dimensional Arrays
NumPy supports matrices and higher-dimensional arrays:
    

"""
1. Debugging a Python Program
# By using this command we can debug a python program

Answer:

python -m pdb python-script.py

2. Yield Keyword in Python
The keyword in Python can turn any function into a generator. Yields work like a standard return keyword.

"""

def days(index):
    day=['S','M','T','W','Tr','F','St']
    yield day[index]
    yield day[index+1]
    
res=days(0)
print(next(res),next(res))


"""
Question 

3. Converting a List into a String
When we want to convert a list into a string, we can use the <.join()> method which joins all the elements into one and returns as a string.

"""

days=['S','M','T','W','Tr','F','St']
ltos=' '.join(days)

print(type(days))
print(type(ltos))
print(ltos)

"""
Question 

4. Converting a List into a Tuple
By using Python <tuple()> function we can convert a list into a tuple. But we can’t change the list after turning it into tuple, because it becomes immutable.

"""
days=['S','M','T','W','Tr','F','St']
ltos=tuple(days)


Dicdays={'S','M','T','W','Tr','F','St'}
print(type(Dicdays))
print(type(days))
print(type(ltos))
print(ltos)


"""
Comments:
    
    look at the brackets while converting from list to tuple and set
    I think set and dictionary can be related
"""


"""
5. Converting a List into a Set
    
    User can convert list into set by using <set()> function.
"""

days=['S','M','T','W','Tr','F','St']
ltos=set(days)

print(ltos)
print(type(ltos))

"""
6. Counting the occurrences of a particular element in the list
    We can count the occurrences of an individual element by using a <count()> function.
    
6.1. Counting the occurrences of elements in the list

"""

days = ['S','M','W', 'M','M','F','S']
print(days.count('M'))

days = ['S','M','M','M','F','S']
y = set(days)

print([[x,days.count(x)] for x in y])


"""
7. Creating a NumPy Array in Python

    NumPy arrays are more flexible then lists in Python

"""

import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)
print(type(arr))

"""
8. Implement a LRU (Least Recently Used) Cache
"""

from collections import OrderedDict

class LRUCache:
    def __init__ (self, capacity:int):
        self.cache=OrderedDict()
        self.capacity=capacity
        
    def get(self, key: int) ->int:
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]
    
    def put(self, key:int, value:int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key]=value
        if len(self.cache)> self.capacity:
            self.cache.popitem(last=False)
            
# Example Usage
lru=LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)
print(lru.get(1)) 
lru.put(3, 3)

"""
9. Find the Longest Substring Without Repeating Characters
"""

def length_of_longest_substring(s: str)->int:
    char_index_map={}
    start=max_length=0
    
    for i, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >=start:
            start= char_index_map[char]+1
        char_index_map[char]=i
        max_length=max(max_length, i- start+1)
        
    return max_length

# Example Usage 
print(length_of_longest_substring("abcabcbb"))


"""
10. Find the Kth Largest Element in an Array
"""

import heapq

def find_kth_largest(nums:list, k: int)-> int:  # Type Hinting
    return heapq.nlargest(k, nums)[-1]

# Example Usage:
print(find_kth_largest([3,2,1,5,6,4], 2))