import unittest
from . import assignment_eight_2021_09_20 as a8

class TestAssignmentEight(unittest.TestCase):
    def test_quicksort(self):
        test = [[1, 3, 2],
                [],
                [2],
                [5, 4, 3, 2, 1],
                [1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2]]
        res = [[1, 2, 3],
                [],
                [2],
                [1, 2, 3, 4, 5],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]]

        for i in range(0, len(test)):
            a8.quick_sort(test[i], 0, len(test[i]) - 1)
            self.assertEqual(test[i], res[i])

if __name__ == "__main__":
    unittest.main()