import unittest
import assignement_one_2021_08_19 as a1

class TestAssignmentOne(unittest.TestCase):
    
    def test_capitalization(self):
        res = [["One"], ["One", "Two three"], ["One", "Two", "Three"]]
        test = [["one"], ["one", "two three"], ["one", "two", "three"]]

        for i in range(0, len(test)):
            self.assertEqual(a1.capitialize_words(test[i]), res[i])

    def test_sum_of_ints(self):
        res = [15, 21, 0, 0, 3]
        test = [6, 7, 0, 1, 3]

        for i in range(0, len(test)):
            self.assertEqual(a1.sum_values(test[i]), res[i])

    def test_sum_fail(self):
        test = -5
        
        with self.assertRaises(ValueError):
            a1.sum_values(test)

if __name__ == '__main__':
    unittest.main()




