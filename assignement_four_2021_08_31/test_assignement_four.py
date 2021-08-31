from . import assignement_four_2021_08_31 as a4
import unittest

class TestAssignmentFour(unittest.TestCase):
    def test_iterative_inverse(self):
        test = [[1, 2, 3, 4, 5],
                [],
                [5, 3, 5, 2, 5, 6]]
        res = [[5, 4, 3, 2, 1],
                [],
                [6, 5, 2, 5, 3, 5]]
        for i in range(0, len(test)):
            a4.invert(test[i])
            self.assertEqual(test[i], res[i])
        
    def test_iterative_inverse_r(self):
        test = [[1, 2, 3, 4, 5],
                [],
                [5, 3, 5, 2, 5, 6]]
        res = [[5, 4, 3, 2, 1],
                [],
                [6, 5, 2, 5, 3, 5]]
        for i in range(0, len(test)):
            a4.invert_r(test[i])
            self.assertEqual(test[i], res[i])

if __name__ == '__main__':
    unittest.main()
