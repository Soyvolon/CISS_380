from car import Car
import json

def main():
    sel = ""
    while sel != "b" and sel != "i" and sel != "binary" and sel != "iterative":
        sel = input("Please select search type:\n"
                + "[b] Binary\n"
                + "[i] Iterative\n").lower()
        
        if sel == "test":
            test()
            return

    id = ""
    while id != "1" and id != "2" and id != "3" and id != "4":
        id = input("Please select a value to serach by:\n"
                    + "1 - Make\n"
                    + "2 - Model\n"
                    + "3 - Mileage\n"
                    + "4 - MPG\n").lower()
    
    key = input("What are you seraching for:\n")

    selector = lambda x: x

    if id == "1":
        selector = lambda x: x.get_make()
    elif id == "2":
        selector = lambda x: x.get_model()
    elif id == "3":
        selector = lambda x: x.get_mileage()
    else:
        selector = lambda x: x.get_mpg()

    cars = []
    with open("car_data.json", "r") as file:
        cars = json.load(file, object_hook=lambda x: Car(**x))

    res = 0
    if sel == "b" or sel == "binary":
        cars.sort(key = selector)

        res = binary_search(cars, key, selector)
    else:
        res = search(cars, key, selector)

    if res == -1:
        print("No item found.")
    else:
        print(cars[res])

def test():
    car1 = Car(make = "Mazda", model = "2013", mileage = 1200, mpg = 35)
    car2 = Car(make = "Mazda", model = "2019", mileage = 200, mpg = 50)

    # compare method test.

    print(car1.compare(car2.get_model))

    cars = []
    with open("car_data.json", "r") as file:
        cars = json.load(file, object_hook=lambda x: Car(**x))

    cars.sort(key = lambda x: (x.get_make(), x.get_model()))

    print_car_list(cars)
    print("\nNon Binary Search\n")
    print(search(cars, cars[2]))
    print(search(cars, 20, key=lambda x: x.get_mpg()))

    print("\n\n")

    print_car_list(cars)
    print("\nBinary Search\n")
    print(binary_search(cars, cars[2]))
    # sorted by make so can only use make
    print(binary_search(cars, "Saturn", key=lambda x: x.get_make()))
    print(binary_search(cars, "Ford", key=lambda x: x.get_make()))


def search(lyst, item, key=None):
    if key is None:
        key = lambda x: x
    
    for i in range(len(lyst)):
        if key(lyst[i]) == item:
            return i

    return -1

def binary_search(lyst, item, key=None):
    if key is None:
        key = lambda x: x

    left = 0
    right = len(lyst)
    while left <= right:
        mid = (left + right) // 2
        val = key(lyst[mid])
        if item == val:
            return mid
        elif item < val:
            right = mid - 1
        else:
            left = mid + 1

    return -1

    
def print_car_list(items):
    # display our input to make sure it got read correctly.
    print(["{a} {b} - {c} miles at {d} mpg".format(a = x.get_make(), b = x.get_model(), c = x.get_mileage(), d = x.get_mpg()) for x in items]) 

if __name__ == "__main__":
    main()