import unittest
import assignement_two_2021_08_24 as a2

class TestAssignmentTwo(unittest.TestCase):
    def test_flatten(self):
        test = [[1, 3, [5, 6]],
                [2, [5, 7], 9],
                [9, [9, [10, 11]]],
                []]
        res = [[1, 3, 5, 6],
               [2, 5, 7, 9],
               [9, 9, 10, 11],
               []]

        for i in range(0, len(test)):
            self.assertEqual(a2.flatten_list(test[i]), res[i])

    def test_gcd(self):
        test = [[25, 30],
                [30, 25],
                [60, 75],
                [12, 36]]
        res = [5, 5, 15, 12]

        for i in range(0, len(test)):
            self.assertEqual(a2.gcd(test[i][0], test[i][1]), res[i])

    def test_gcd_err(self):
        with self.assertRaises(ValueError):
            a2.gcd(-1, 2)

        with self.assertRaises(ValueError):
            a2.gcd(2, -1)

if __name__ == '__main__':
    unittest.main()
