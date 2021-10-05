import unittest
from . import assignement_eight_2021_09_28 as a8

class TestArraysClass(unittest.TestCase):
    def test_array_sum(self):
        test = [([1,2,3,4,5,6,7,8,9], 5),
                ([1,2,3,4,5,6,7,8,9], 100),
                ([1,2,3,4,5,6,7,8,9], 6)]
        res = [(1, 2), (-1,), (0, 2)]

        for i in range(0, len(test)):
            self.assertEqual(a8.partial_array_sum(test[i][0], test[i][1]), res[i])
    def test_eq(self):
        test = [([0, 1, 2, None], [0, 1, 2]),
                (["hi", 2, None, None], ["hi", 2, None]),
                (["ni"], ["there"]),
                ([2, None], [2, 3])]
        res = [True, True, False, False]

        for i in range(0, len(test)):
            a1 = a8.Array(len(test[i][0]))
            a2 = a8.Array(len(test[i][1]))
            for x in range(0, len(test[i][0])):
                if test[i][0][x] != None:
                    a1.insert(x, test[i][0][x])
            for x in range(0, len(test[i][1])):
                if test[i][1][x] != None:
                    a2.insert(x, test[i][1][x])

            self.assertEqual(a1 == a2, res[i])

    def test_pop(self):
        test = [([0, 1, 2], 1),
                ([4, 1, 7, 9], 3),
                ([0, 1], 0)]
        
        res = [(1, [0, 2, None]),
                (9, [4, 1, 7, None]),
                (0, [1, None])]
        
        for i in range(0, len(test)):
            a1 = a8.Array(len(test[i][0]))
            for x in range(0, len(test[i][0])):
                a1.insert(x, test[i][0][x])
            
            output = a1.pop(test[i][1])
            self.assertEqual(output, res[i][0])
            count = 0
            for x in a1:
                self.assertEqual(x, res[i][1][count])
                count += 1

    def test_pop_err(self):
        with self.assertRaises(IndexError):
            # below 0
            a1 = a8.Array(2)
            a1.pop(-1)
        with self.assertRaises(IndexError):
            # above the logical cap
            a1 = a8.Array(2)
            a1.pop(10)

    def test_insert(self):
        test = [([0, 1, 2], (1, 3)),
                ([], (3, 1)),
                ([0, 1], (0, 0))]
        res = [[0, 3, 1, 2, None, None],
                [1],
                [0, 0, 1, None]]
        
        for i in range(0, len(test)):
            a1 = a8.Array(len(test[i][0]))
            for x in range(0, len(test[i][0])):
                a1.insert(x, test[i][0][x])
            
            a1.insert(test[i][1][0], test[i][1][1])
            count = 0
            for x in a1:
                self.assertEqual(x, res[i][count])
                count += 1

    def test_insert_err(self):
        with self.assertRaises(IndexError):
            # below 0
            a1 = a8.Array(2)
            a1.insert(-1, 5)

if __name__ == "__main__":
    unittest.main()