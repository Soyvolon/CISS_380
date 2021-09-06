import random
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
    equ = run_equality_checks(gen)

    one = test_one(gen)
    two = test_two(gen)
    three = test_three(gen)

def test_one(gen: PermGenerator) -> str:
    pass

def test_two(gen: PermGenerator) -> str:
    pass

def test_three(gen: PermGenerator) -> str:
    pass

def run_equality_checks(gen: PermGenerator) -> str:
    pass

def gen_test_set():
    output = []
    for i in range(10):
        output.append(int(1000 * random.uniform(-1.15, 1.15)))
    for i in range(0, len(output)):
        if output[i] <= 0:
            output[i] = 1
    return output

if __name__ == "__main__":
    main()