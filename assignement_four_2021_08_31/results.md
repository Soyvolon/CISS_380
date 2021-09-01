# Reverse List Comparisons
> By Andrew Bounds<br />
For `assignement_four_2021_08_31.py`

| Function         | Time Complexity | Size Complexity |
|------------------|-----------------|-----------------|
| Custom Recursive | O(n)            | n               |
| Custom Iterative | O(n)            | 1               |
| Python Builtin   | O(n)            | 1               |

The Custom Recursive function also has the detriment of failing
once a list of items lands between 1950 and 2000 items, on top
of having an `n` level size complexity. Compared to the other two
functions, witch are both edit in place (no new list is created)
and have a time complexity of O(n).

However, even with a time complexity of O(n), the builtin python
function works better than my custom function as somewhere in its
designs it works more efficiently.

Take these two sets of data for example:
| Function         | Completion Time       | Data Size | Sets Run |
|------------------|-----------------------|-----------|----------|
| Custom Iterative | 0.03789258003234863   | 900000    | 1        |
| Python Builtin   | 0.0010166168212890625 | 900000    | 1        |
|------------------|-----------------------|-----------|----------|
| Custom Iterative | 0.041887521743774414  | 1000000   | 1        |
| Python Builtin   | 0.00193023681640625   | 1000000   | 1        |

| Function         | Completion Time       | Data Size | Sets Run |
|------------------|-----------------------|-----------|----------|
| Custom Iterative | 0.02495884895324707   | 50        | 10000    |
| Python Builtin   | 0.0020558834075927734 | 50        | 10000    |
|------------------|-----------------------|-----------|----------|
| Custom Iterative | 0.04280376434326172   | 100       | 10000    |
| Python Builtin   | 0.0                   | 100       | 10000    |
|------------------|-----------------------|-----------|----------|
| Custom Iterative | 3.332547664642334     | 5000      | 10000    |
| Python Builtin   | 0.01994490623474121   | 5000      | 10000    |

As you can see, the efficiency of the custom iterative and python
builtin functions are comparable at a single-large data set and
a large amount of small data sets, but as soon as it becomes
a large amount of larger data sets, the python function clearly
becomes the more efficient function.

Even with the same time complexity, the use of size checking in
the custom function extends the completion time, especially for
a large amount of large sets of data.

> Additional data sets can be found in the `output_*.md` files.