import random
import math
import time

class PermGenerator():
    def __init__(self, seed = None):
        if seed is None:
            self.__rand = random.Random()
        else:
            self.__rand = random.Random(seed)

    def fill_perm_one(self, size: int) -> list:
        output = []
        for i in range(size):
            val = -1
            while val < 0 or val in output:
                val = self.__rand.randint(1, size)
            output.append(val)
        return output

    def fill_perm_two(self, size: int) -> list:
        output = []
        size_range = range(size)
        # needs to be one item larger
        used = [False for x in range(size + 1)]
        for i in size_range:
            val = -1
            while val < 0:
                tmp = self.__rand.randint(1, size)
                try:
                    if(used[tmp]):
                        continue
                    else:
                        val = tmp
                except:
                    val = tmp
            output.append(val)
            used[val] = True
        return output
    
    def fill_perm_three(self, size: int) -> list:
        size_range = range(size)
        rand_size = size - 1
        output = [x + 1 for x in size_range]
        for i in size_range:
            other = self.__rand.randint(1, rand_size)
            output[i], output[other] = output[other], output[i]
        return output

    def validate_perm(self, perm: list) -> bool:
        data = set()
        for item in perm:
            if not item in data:
                data.add(item)
            else:
                return False
        return True


def main():
    gen = PermGenerator()
    rand = test_randomness(gen)

    one = test(gen, [250, 500, 1000, 2000], 10)
    two = test(gen, [2500, 5000, 10000, 20000, 40000, 80000], 10)
    three = test(gen, [10000, 20000, 40000, 80000, 160000, 320000, 640000], 10)
    
    with open("comp_output.md", "wt") as file:
        file.write(rand + "\n\n" + one + "\n\n" + two + "\n\n" + three)

def test(gen: PermGenerator, data: list, runs: int) -> str:
    data = [x for x in data for y in range(0, runs)]
    output = [[], [], []]
    for item_c in range(len(data)):
        output[0].append([data[item_c]])
        output[1].append([data[item_c]])
        output[2].append([data[item_c]])
        print("starting set {a} [{b}]".format(a = item_c, b = data[item_c]))
        
        output[0][item_c].append(get_runtime(gen.fill_perm_one, data[item_c]))
        output[1][item_c].append(get_runtime(gen.fill_perm_two, data[item_c]))
        output[2][item_c].append(get_runtime(gen.fill_perm_three, data[item_c]))

        print("ran set {a} [{b}]".format(a = item_c, b = data[item_c]))

    outData = ""

    for x in range(len(output)):
        title = "\n### Algorithm {a}\n".format(a = x + 1)
        print(title)
        outData += title
        outData += "| Size (n) | Runtime (s) |\n"
        outData += "|----------|-------------|\n"
        for i in range(len(output[x])):
            
            length = output[x][i][0]
            ttc = output[x][i][1]

            outData += "| {a} | {b} |\n".format(a = length, b = ttc)

    return outData

def test_randomness(gen: PermGenerator) -> str:
    data = gen_test_set()
    output = [[], [], []]
    for item_c in range(len(data)):
        output[0].append([])
        output[1].append([])
        output[2].append([])
        fact = math.factorial(data[item_c])
        print("starting set {a} [{c}]: n! where n is {b}".format(a = item_c, b = fact, c = data[item_c]))
        for i in range(fact):
            output[0][item_c].append(gen.fill_perm_one(data[item_c]))
            output[1][item_c].append(gen.fill_perm_two(data[item_c]))
            output[2][item_c].append(gen.fill_perm_three(data[item_c]))
        print("ran set {a} [{c}]: n! where n is {b}".format(a = item_c, b = fact, c = data[item_c]))

    outData = ""

    for x in range(len(output)):
        title = "\n### Algorithm {a}\n".format(a = x + 1)
        print(title)
        outData += title
        outData += "|Size (n)|n!|Repeats|Repeat %|Over Half|\n"
        outData += "|--------|--|-------|--------|---------|\n"
        for i in range(len(output[x])):
            fact = len(output[x][i])
            size = len(output[x][i][0])

            repeats = 0
            data = set()
            for item in output[x][i]:
                val = tuple(item)
                if not val in data:
                    data.add(val)
                else:
                    repeats += 1

            repper = repeats / fact
            outData += "|{a}|{b}|{c}|{d}|{e}|\n".format(a = size, b = fact, c = repeats, d = repper, e = repper >= 0.5)

    with open("randomness_output.md", "wt") as file:
        file.write(outData)

    return outData

def get_runtime(func, *args):
    start = time.time()
    func(*args)
    return time.time() - start


def gen_test_set():
    return [x for x in range(2, 9) for y in range(0, 10)]

if __name__ == "__main__":
    main()