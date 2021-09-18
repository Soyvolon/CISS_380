import unittest
from . import cycle_sort as c

class TestAssignmentSeven(unittest.TestCase):
    def test_cyc_sort(self):
        data = [[1,3,5,3,2],
                [],
                [22,22,22,33,11,11,11,22,11,22,33],
                [1,2,3,4,5],
                ["a", "b", "a", "c"]]
        res = [[1,2,3,3,5],
                [],
                [11,11,11,11,22,22,22,22,22,33,33],
                [1,2,3,4,5],
                ["a", "a", "b", "c"]]

        for i in range(0, len(data)):
            test = data[i]
            c.cycle_sort(test)
            self.assertEqual(test, res[i])

if __name__ == "__main__":
    unittest.main()