# Circle Sort Analysis

## Complexity

|              | Time Compexity | Space Complexity |
|--------------|----------------|------------------|
| Best Case    | O(n^2)         | O(1)             |
| Average Case | O(n^2)         | n/a              |
| Worst Case   | O(n^2)         | O(n)             |

## Analysis

With random testing the circle sort still falls under a time complexity of `O(n^2)` no matter how the inital list is ordered because it checks the entire set of data for each element twice when deterining if an item needs to be moved or not. Take the following time comparions for example:

| Data Size | Time (s)           | Data Size | Time (s)           |
|-----------|--------------------|-----------|--------------------|
| 700       | 2.535173177719116  | 1400      | 7.240840673446655  |
| 700       | 2.202059507369995  | 1400      | 6.846515655517578  |
| 700       | 1.8363163471221924 | 1400      | 6.7514121532440186 |
| 700       | 1.6750454902648926 | 1400      | 6.800145864486694  |
| 700       | 1.6305222511291504 | 1400      | 6.643028974533081  |

The time comparison here shows a drastic increaes in time, much more than doubling even though the data size between these two sets of tests has only doubled. Simillar results can be sen more starkly with larger data sizes:

| Data Size | Time (s)           | Data Size | Time (s)           |
|-----------|--------------------|-----------|--------------------|
| 1000      | 3.6110401153564453 | 2000      | 16.670913457870483 |
| 1000      | 3.392928123474121  | 2000      | 15.916614055633545 |
| 1000      | 3.544827938079834  | 2000      | 16.870020866394043 |
| 1000      | 3.3242883682250977 | 2000      | 15.372862577438354 |
| 1000      | 3.516788959503174  | 2000      | 15.372260570526123 |