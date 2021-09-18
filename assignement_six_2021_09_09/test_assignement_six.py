import unittest
from . import assignement_six_2021_09_09 as a6

class TestAssignmentSix(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.__data = [a6.Car(make = "Mazda", model = "2013", mileage = 200, mpg = 10),
            a6.Car(make = "Toyota", model = "Camry", mileage = 300, mpg = 20),
            a6.Car(make = "Ford", model = "F150", mileage = 100, mpg = 5),
            a6.Car(make = "Saturn", model = "Vue", mileage = 400, mpg = 15)]

    def test_int_compare(self):
        res = [-1, 0, -1, 0]

        # check make
        self.assertTrue(self.__data[2].compare(self.__data[3], 0), res[0])
        # check model
        self.assertTrue(self.__data[0].compare(self.__data[0], 1), res[1])
        # check mileage
        self.assertTrue(self.__data[0].compare(self.__data[1], 2), res[2])
        # check mpg
        self.assertTrue(self.__data[3].compare(self.__data[3], 3), res[3])

    def test_method_compare(self):
        pass

    def test_iter_search(self):
        pass

    def test_binary_search(self):
        pass

if __name__ == "__main__":
    unittest.main()