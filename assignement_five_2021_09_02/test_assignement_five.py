from . import assignement_five_2021_09_02 as a5
import unittest
import random

class TestAssignmentFive(unittest.TestCase):
    def setUp(self):
        self.__permGen = a5.PermGenerator()
        self.__rand = random.Random()
        self.__dataSize = 1000
        self.__dataClusters = 5
        self.__dataVariation = 0.2

    def test_validate_perm(self):
        data = [[1, 2, 3, 4, 5],
                [1, 2, 1],
                [1],
                []]
        res = [True, False, True, True]

        for i in range(0, len(data)):
            val = self.__permGen.validate_perm(data[i])
            self.assertEqual(val, res[i])

    def test_perm_func_one(self):
        data = self.gen_test_set()
        for i in range(0, len(data)):
            res = self.__permGen.fill_perm_one(data[i])
            self.assertTrue(self.__permGen.validate_perm(res))

    def test_perm_func_two(self):
        data = self.gen_test_set()
        for i in range(0, len(data)):
            res = self.__permGen.fill_perm_two(data[i])
            self.assertTrue(self.__permGen.validate_perm(res))

    def test_perm_func_three(self):
        data = self.gen_test_set()
        for i in range(0, len(data)):
            res = self.__permGen.fill_perm_three(data[i])
            self.assertTrue(self.__permGen.validate_perm(res))

    def gen_test_set(self):
        output = []
        for i in range(self.__dataClusters):
            output.append(int(self.__dataSize * self.__rand.uniform(1 + -self.__dataVariation, 1 + self.__dataVariation)))
        for i in range(0, len(output)):
            if output[i] <= 0:
                output[i] = 1
        return output

    def tearDown(self):
        self.__permGen = None

if __name__ == "__main__":
    unittest.main()