# Suppose that you once had a permutation of numbers from 1 to n 
# (a permutation is just any rearrangement of a set of items). However, your big 
# and bad roommate came and stole some of the numbers in your permutation the number 
# of stolen elements can be anything between none and all). Fortunately, the order of 
# the remaining elements was preserved. You are to write a python program that will
# try to reconstruct the original permutation.  If there are multiple options return
# lexicographically smallest among them. (given two permutations of numbers 1 through 
# n the one that has smaller value at the first index they differ is lexicographically 
# smaller). There are two inputs to your program. One input is number n and the other 
# input is the list or remaining elements in the permutation. 

# You may assume that n is not larger than 10. 

# For example assume that n = 5 and the list of remaining items is [1, 4, 2]. 
# the output in this case should be [ 1, 3, 4, 2, 5] In this case there are two 
# numbers missing (3 and 5) and 20 possible ways to add them back. [1, 3, 4, 2, 5] 
# is the lexicographically smallest among them. 

"""
Assignemnt Three 2021-08-26

@author: Andrew Bounds
"""

def main():
    print(fill_permutation([1, 4, 2], 5))

def fill_permutation(items, values):
    data = items[:]
    for x in range(1, values + 1):
        if not x in data:
            slot_value(data, x)
    return data

def slot_value(data, value):
    if len(data) != 0:
        for i in range(0, len(data)):
            if value < data[i]:
                data.insert(i, value)
                return

    data.append(value)

if __name__ == "__main__":
    main()