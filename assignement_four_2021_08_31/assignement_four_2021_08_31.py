""" Assignmenet Four 2021-08-31

@author: Andrew Bounds
"""

import time
import random as _rand
import profile as profile

def main():
    test_data = gen_test_data()

    output = """
|Function|Time (s)|Data Size (n)|Batch Size (runs)|Time Complexity|Size Complexity|
|--------|--------|-------------|-----------------|---------------|---------------|"""
    data_max = 10000
    for data in test_data:

        runs = data_max
        if runs <= 0:
            runs = 1
        iter_end = 0
        for x in range(runs):
            iter_start = time.time()
            invert(data)
            iter_end += time.time() - iter_start

        output += """
|{a}|{b}|{c}|{d}|{e}|{f}|""".format(a = "Iter Reverse", b = iter_end, c = len(data), d = runs, e = "O(n)", f = "1")

        try:
            r_end = 0
            for x in range(runs):
                r_start = time.time()
                invert_r(data)
                r_end += time.time() - r_start

            output += """
|{a}|{b}|{c}|{d}|{e}|{f}|""".format(a = "Recursive Reverse", b = r_end, c = len(data), d = runs, e = "O(n)", f = "n")
        except:
            r_end = time.time() - r_start
            output += """
|{a}|{b}|{c}|{d}|{e}|{f}|""".format(a = "Recursive Reverse", b = r_end, c = len(data), d = "ERRORED", e = "ERRORED", f = "n")

        internal_end = 0
        for x in range(runs):
            internal_start = time.time()
            data.reverse()
            internal_end += time.time() - internal_start

        output += """
|{a}|{b}|{c}|{d}|{e}|{f}|""".format(a = "Python Reverse", b = internal_end, c = len(data), d = runs, e = "O(n)", f = "1")

    with open("output.md", "wt") as file:
        file.write(output)

    print("Output written to output.md")

def gen_test_data(test_sets = 100, set_size_base = 50):
    data = []
    for m in range(1, test_sets + 1):
        data.append([])
        for i in range(0, set_size_base * m):
            data[m - 1].append(_rand.randint(0, 100))

    return data

def invert(items):
    leng = len(items) - 1
    if leng <= 0: return
    cap = int(leng / 2) + 1
    for i in range(0, cap):
        diff = leng - i
        items[i], items[diff] = items[diff], items[i]
        

def invert_r(items, point = 0):
    leng = len(items)
    if leng == 0: return
    end = (leng - 1) - point
    if point >= leng / 2: return
    items[point], items[end] = items[end], items[point]
    invert_r(items, point + 1)

if __name__ == "__main__":
    main()