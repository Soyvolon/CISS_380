
def main():
    selection = input("Select operation (input the number):\n\n" + 
          "1. Capitilazation Method\n" +
          "2. Sum of Integers\n\n")
    while selection != "1" and selection != "2":
        selection = input("No valid option was selected. Please input 1 or 2.\n\n" + 
                          "Select operation (input the number):\n\n" + 
                          "1. Capitilazation Method\n" +
                          "2. Sum of Integers\n\n")

    if selection == "1":
        caps_main()
    elif selection == "2":
        sum_main()

def caps_main():
    selection = input("\n\n---- CAPITILZATION ----\n\nEnter a list of words, separated by spaces:\n")

    parts = selection.split(" ")

    res = capitialize_words(parts)

    print("The new list: {r}".format(r = res))

def capitialize_words(words, index: int = 0, res = []):
    if index < len(words):
        res.append(words[index].capitalize())
        return capitialize_words(words, index + 1, res)
    else:
        return res

def sum_main():
    selection = input("\n\n---- INTEGER SUM ----\n\nEnter an integer above 0:\n")

    val, res = try_parse_int(selection)
    while not res or val <= 0:
        val, res = try_parse_int(input("An integer was not entered. Please enter a numberical value above 0:\n"))
    
    sum = sum_values(val)

    print("The sum of all values below {s} and above 0 is: {res}".format(s = val - 1, res = sum))

def sum_values(current: int, sum: int = 0) -> int:
    if current < 0:
       raise ValueError("current must be above 0.")
    elif current == 0:
        return sum
    else:
        next = current - 1
        return sum_values(next, sum + next)

def try_parse_int(val):
    try:
        return int(val), True
    except:
        return -1, False

if __name__ == "__main__":
    main()