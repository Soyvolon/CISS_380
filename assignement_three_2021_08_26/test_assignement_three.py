
import unittest
from . import assignement_three_2021_08_26 as a3

class TestAssigmentThree(unittest.TestCase):
    def test_permutation(self):
        test = [[[1, 3, 2], 5],
                [[4, 7, 3, 2], 10],
                [[2, 9, 3, 8], 9],
                [[], 3],
                [[1, 4, 2], 5]]
        res = [[1, 3, 2, 4, 5],
               [1, 4, 5, 6, 7, 3, 2, 8, 9, 10],
               [1, 2, 4, 5, 6, 7, 9, 3, 8],
               [1, 2, 3],
               [1, 3, 4, 2, 5]]

        for i in range(0, len(test)):
            self.assertEquals(a3.fill_permutation(test[i][0], test[i][1]), res[i])

if __name__ == "__main__":
    unittest.main()