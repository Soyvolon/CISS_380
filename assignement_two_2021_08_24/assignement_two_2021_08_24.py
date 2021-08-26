"""
HW 2021-08-24

@author: Andrew Bounds
"""

def main():
    selection = input("Select operation (input the number):\n\n" + 
          "1. Flatten List Method\n" +
          "2. GCD\n\n")
    while selection != "1" and selection != "2":
        selection = input("No valid option was selected. Please input 1 or 2.\n\n" + 
                          "Select operation (input the number):\n\n" + 
                          "1. Flatten List Method\n" +
                          "2. GCD\n\n")

    if selection == "1":
        flatten_main()
    elif selection == "2":
        gcd_main()

def flatten_main():
    data = [1, 2, [3, 4, [5, 6, [7]]]]
    output = flatten_list(data)
    print("Turned {a} into {b}".format(a = data, b = output))

def flatten_list(data):
    if len(data) <= 0:
        return data
    elif type(data[0]) == list:
        return flatten_list(data[0]) + flatten_list(data[1:])
    return data[:1] + flatten_list(data[1:])

def gcd_main():
    one = input("Input the first non-negative number:\n")
    while(type(one) != int):
        try:
            one = int(one)

            if one < 0:
                one = input("Not a non-negative number. Please input the first non-negative number:\n")
        except:
            one = input("Not a number. Please input the first non-negative number:\n")
        
    two = input("Input the second non-negative number:\n")
    while(type(two) != int):
        try:
            two = int(two)

            if two < 0:
                two = input("Not a non-negative number. Please input the second non-negative number:\n")
        except:
            two = input("Not a number. Please input the second non-negative number:\n")

    output = gcd(one, two)

    print("GCD of {a} and {b} is {c}".format(a = one, b = two, c = output))

def gcd(a, b):
    if a < 0:
        raise ValueError("A must be non-negative.")
    if b < 0:
        raise ValueError("B must be non-negative.")
    if a < b:
        return gcd(b, a)
    elif b == 0:
        return a
    else:
       return gcd(b, a % b)

if __name__ == "__main__":
    main()