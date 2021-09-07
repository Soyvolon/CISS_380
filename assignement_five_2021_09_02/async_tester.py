import assignement_five_2021_09_02 as a5
import threading
import time

# I offically hate python async

class TestThreader(threading.Thread):
    def __init__(self, test_set, runs, method, result_cache):
        threading.Thread.__init__(self)
        self.__data = test_set
        self.__runs = runs
        self.__method = method
        self.__res = result_cache

    def run(self):
        print("starting test threader.")
        data = [x for x in self.__data for y in range(0, self.__runs)]

        for i in data:
            self.__res.append([i])

        runners = []

        for i in range(0, len(data)):
            runners.append(RuntimeThreader(self.__method, self.__res[i], data[i]))

        for i in runners:
            i.start()

        for i in runners:
            i.join()

        print("completed test threader.")

class RuntimeThreader(threading.Thread):
    def __init__(self, method, output, *args):
        threading.Thread.__init__(self)
        self.__method = method
        self.__args = args
        self.__output = output

    def run(self):
        data = self.get_runtime(self.__method, *self.__args)
        self.__output.append(data)

    def get_runtime(self, func, *args):
        start = time.time()
        func(*args)
        return time.time() - start

def main():
    output = []
    gen = a5.PermGenerator()
    tester = TestThreader([100, 500, 1000, 10000], 5, gen.fill_perm_one, output)
    tester.start()
    threading.Thread.join(tester)
    print("Test data grabbed.")
    print(output)

if __name__ == "__main__":
    main()