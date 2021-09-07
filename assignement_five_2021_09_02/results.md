# Randomness and Validation

While proving that all three algorithms produce an equally likely set of permutations is difficult to do programmatically, proving that the algorithms produce valid permutations is simple as the following method:

```py
def validate_perm(self, perm: list) -> bool:
    data = set()
    for item in perm:
        if not item in data:
            data.add(item)
        else:
            return False
    return True
```

Running the generators through a set of tests (see: `test_assignement_five.py`) with random data set sizes allows us to say there is no statistically significant evidence that these three methods generate invalid permutations.

While not a fully accurate test, the data in `randomness_output.md` does show that while there is randomness in the three different methods, and each method *does* create a permutation with equally likely chance of a value being in any position in the permutation (due to the use of `random.randint()` to determine order), the limitations of the sudo random number generator python uses makes the randomness of multiple runes of the permutation generator quite low in some cases. Granted, this test data is run on small data sizes for speed, as larger permutation sizes using this method would require exceptionally long runtimes.

A short snippet of data from the randomness output file follows:
### Algorithm 1
| Size (n) | n!    | Repeats | Repeat %            | Over Half |
|----------|-------|---------|---------------------|-----------|
| 7        | 5040  | 1865    | 0.37003968253968256 | False     |
| 8        | 40320 | 14869   | 0.3687748015873016  | False     |

### Algorithm 2
| Size (n) | n!    | Repeats | Repeat %            | Over Half |
|----------|-------|---------|---------------------|-----------|
| 7        | 5040  | 1868    | 0.37063492063492065 | False     |
| 8        | 40320 | 14821   | 0.3675843253968254  | False     |

### Algorithm 3
| Size (n) | n!    | Repeats | Repeat %            | Over Half |
|----------|-------|---------|---------------------|-----------|
| 7        | 5040  | 2111    | 0.41884920634920636 | False     |
| 8        | 40320 | 16882   | 0.41870039682539684 | False     |

<hr />

# Expected (Big-O) Runtime

### Algorithm 1
```
O(n^3)
```
For every top level item (n), we have to check the entire list for it (n), and if it is in the list, we generate a new value and try again, for a maximum of (n) attempts.
### Algorithm 2
```
O(n^2)
```
For every top level item (n), we have to check a hash set like data for it (1), and if it is in the list, we generate a new value and try again, for a maximum of (n) attempts.
### Algorithm 3
```
O(2n)
```
For every top level item (n) we generate an output set for it. **Afterwards**, for every item in the output set, we swap its place with another item in the set (n).
<hr />

# Actual Runtime

### Algorithm 1
### Algorithm 2
### Algorithm 3