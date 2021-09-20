# Modify the quicksort function so that it calls insertion sort to sort any sublist whose 
# size is less than 50 items. Compare the performance of this version with that of the 
# original one, using data sets of 100, 1000, and 10000 items. Then adjust the threshold 
# for using the insertion sort to determine an optimal setting

import random
import time

def quick_sort(arr, low, high, split = 50):
    if len(arr) <= 1:
        return

    if low < high:
        part = partition(arr, low, high, split)

        quick_sort(arr, low, part - 1, split)
        quick_sort(arr, part + 1, high, split)

def partition(arr, low, high, split):
    set = range(low, high)

    if(len(set) < split):
        for i in set:
  
            key = arr[i + 1]
    
            j = i
            while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
    else:
        i = low - 1
        pivot = arr[high]
        for j in set:
            if arr[j] <= pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def main():
    test_data = [100, 1000, 10000]
    splits = [x * 5 for x in range(1, 25)]
    for i in test_data:
        larger_data_set = []
        for split in splits:
            split_set = []
            for a in range(20):
                indexies = [x for x in range(i)]
                data_set = [0 for x in range(i)]
                for x in range(i):
                    index = indexies.pop(random.randint(0, len(indexies) - 1))
                    data_set[index] = x
                split_set.append(data_set)
            larger_data_set.append((split_set, split))

        run_sort_test(larger_data_set)

def run_sort_test(test_data):
    size = len(test_data[0][0][0])
    times = []
    for i in test_data:
        low = 0
        high = size - 1
        start = time.time()
        for split in i[0]:
            quick_sort(split, low, high, i[1])
    
        times.append(time.time() - start)
    
    output = "|Size (n)|Split Value|Time (s)|\n|-|-|-|\n"
    for x in range(0, len(times)):
        output += "|{a}|{b}|{c}|\n".format(a = size, b = test_data[x][1], c = times[x])
    
    with open("sort_test_{a}".format(a = size), "wt") as file:
        file.write(output)

if __name__ == "__main__":
    main()