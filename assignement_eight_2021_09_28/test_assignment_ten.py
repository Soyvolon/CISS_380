import unittest
from . import assignment_ten_2021_10_05 as a10

class TestIntArray(unittest.TestCase):
    def _build_int_array(self, lyst):
        pass

    def test_addition(self):
        test = [([1, 2, 3], [3, 2, 1]),
                ([0, 3], [1, 2, 3]),
                ([], [1, 2, 3])]
        res = [[4, 4, 4],
                [1, 5, 3],
                [1, 2, 3]]
        
        for i in range(0, len(test)):
            a1 = a10.IntArray(len(test[i][0]))
            a2 = a10.IntArray(len(test[i][1]))
            for x in range(0, len(test[i][0])):
                a1.insert(x, test[i][0][x])
            for x in range(0, len(test[i][1])):
                a2.insert(x, test[i][1][x])

            output = a1 + a2

            for x in range(0, len(output)):
                self.assertEqual(res[i][x], output[x])

    def test_non_int_fail_add(self):
        with self.assertRaises(ValueError):
            a1 = a10.IntArray(2)
            a1 + "hi"

    def test_subtraction(self):
        test = [([1, 2, 3], [3, 2, 1]),
                ([0, 3], [1, 2, 3]),
                ([], [1, 2, 3])]
        res = [[-2, 0, 2],
                [-1, 1, -3],
                [-1, -2, -3]]
        
        for i in range(0, len(test)):
            a1 = a10.IntArray(len(test[i][0]))
            a2 = a10.IntArray(len(test[i][1]))
            for x in range(0, len(test[i][0])):
                a1.insert(x, test[i][0][x])
            for x in range(0, len(test[i][1])):
                a2.insert(x, test[i][1][x])

            output = a1 - a2

            for x in range(0, len(output)):
                self.assertEqual(res[i][x], output[x])

    def test_non_int_fail_sub(self):
        with self.assertRaises(ValueError):
            a1 = a10.IntArray(2)
            a1 - "hi"

    def test_mul(self):
        test = [([1, 2, 3], 2),
                ([0, 3], -1),
                ([5, 25], 5)]
        res = [[2, 4, 6],
                [0, -3],
                [25, 125]]
        
        for i in range(0, len(test)):
            a1 = a10.IntArray(len(test[i][0]))
            for x in range(0, len(test[i][0])):
                a1.insert(x, test[i][0][x])

            output = a1 * test[i][1]

            for x in range(0, len(output)):
                self.assertEqual(res[i][x], output[x])
            
    def test_non_int_fail_mul(self):
        with self.assertRaises(ValueError):
            a1 = a10.IntArray(2)
            a1 * "hi"

    def test_truediv(self):
        test = [([1, 2, 3], 2),
                ([0, 3], -1),
                ([5, 25], 5)]
        res = [[0, 1, 1],
                [0, -3],
                [1, 5]]
        
        for i in range(0, len(test)):
            a1 = a10.IntArray(len(test[i][0]))
            for x in range(0, len(test[i][0])):
                a1.insert(x, test[i][0][x])

            output = a1 / test[i][1]

            for x in range(0, len(output)):
                self.assertEqual(res[i][x], output[x])
    def test_non_int_fail_truediv(self):
        with self.assertRaises(ValueError):
            a1 = a10.IntArray(2)
            a1 / "hi"

    def test_floordiv(self):
        test = [([1, 2, 3], 2),
                ([0, 3], -1),
                ([5, 25], 5)]
        res = [[0, 1, 1],
                [0, -3],
                [1, 5]]
        
        for i in range(0, len(test)):
            a1 = a10.IntArray(len(test[i][0]))
            for x in range(0, len(test[i][0])):
                a1.insert(x, test[i][0][x])

            output = a1 // test[i][1]

            for x in range(0, len(output)):
                self.assertEqual(res[i][x], output[x])
    def test_non_int_fail_floordiv(self):
        with self.assertRaises(ValueError):
            a1 = a10.IntArray(2)
            a1 // "hi"

    def test_exp(self):
        test = [([1, 2, 3], 2),
                ([5, 25], 5)]
        res = [[1, 4, 9],
                [3125, 9765625]]
        
        for i in range(0, len(test)):
            a1 = a10.IntArray(len(test[i][0]))
            for x in range(0, len(test[i][0])):
                a1.insert(x, test[i][0][x])

            output = a1 ** test[i][1]

            for x in range(0, len(output)):
                self.assertEqual(res[i][x], output[x])
    def test_non_int_fail_exp(self):
        with self.assertRaises(ValueError):
            a1 = a10.IntArray(2)
            a1 ** "hi"

    def test_non_int_res_fail_exp(self):
        with self.assertRaises(ValueError):
            a1 = a10.IntArray(2)
            a1.insert(0, 1)
            a1.insert(1, 2)

            a1 ** -1

    def test_non_int_fail_init(self):
        with self.assertRaises(ValueError):
            a10.IntArray(2, None)

if __name__ == "__main__":
    unittest.main()