# Suppose that you have an array of n positive integers. You are also given a positive 
# integer x. Can you find a part of the array consisting of consecutive elements such that 
# these elements add up to x? Let's look at an example. 

# Suppose that the array is [1,2,3,4,5,6,7,8,9] and x is 5. In this case the part of 
# the array consisting of second and third element, that is [2,3] adds up to 5. I could 
# also take a sub-array that consist of a single element  [5] that also have this property. 
# On the other hand, with the same array and x = 100 there is no solution. There is no way 
# to choose a collection of consecutive elements in that array that would add up to 100. 

# You are to write a Python function partialArraySum(arr, x) that will take two parameters. 
# The first parameter arr should be an Array of positive integers (an object of the Array 
# class defined in the attached python module), the second parameter x is a positive integer 
# that represents the desired sum. This function should return a tuple of two array indexes that 
# indicate the starting and ending index of that part of an array where elements add up to x. 
# If no part of the array arr adds up to x the function should return a tuple with one element 
# which is number -1. In the case that more than one part of the array adds to x, the function 
# should return the part that starts at the smallest index. For example

# partialArraySum([1,2,3,4,5,6,7,8,9], 5) 

# should return (1,2) since the part of the array that consist of elements at indexes 1 and 2 adds up to 5. On the other hand

# partialArraySum([1,2,3,4,5,6,7,8, 9], 100) 

# should return (-1,) since no part of the array adds to 100. 

from typing import Tuple
if __name__ == "__main__":
    # for running from this file
    from arrays import Array
else:
    # for running from test cases where this is in a module
    from .arrays import Array

def partial_array_sum(arr: Array, x: int) -> Tuple:
    for start in range(0, len(arr)):
        sum = arr[start]
        for end in range(start + 1, len(arr)):
            sum += arr[end]
            if sum == x:
                return (start, end)
    return (-1,)

def main():
    a = partial_array_sum([1,2,3,4,5,6,7,8,9], 5)
    b = partial_array_sum([1,2,3,4,5,6,7,8,9], 100)
    print(a)
    print(b)

if __name__ == "__main__":
    main()