import async_tester as test
import assignement_five_2021_09_02 as a5

def main():
    gen = a5.PermGenerator()
    data = [10000, 20000, 40000, 80000, 160000, 320000, 640000]
    output = [[]]
    tester = []
    #tester.append(test.TestThreader(data, 10, gen.fill_perm_one, output[0]))
    #tester.append(test.TestThreader(data, 10, gen.fill_perm_two, output[1]))
    tester.append(test.TestThreader(data, 10, gen.fill_perm_three, output[0]))
    
    for i in tester:
        i.start()

    for i in tester:
        i.join()

    print("testers completed, compiling results...")

    # order by data set size

    output.sort(key = lambda x: x[0])

    print(output)

    dataString = "Test Three Results"
    c = 1
    for s in output:
        dataString += "\n### Algorithm 3\n"
        c += 1
        dataString += "| Size (n) | Time (s) |\n"
        dataString += "|----------|----------|\n"
        for i in s:
            dataString += "| {a} | {b} |\n".format(a = i[0], b = i[1])
    
    with open("test_three_res.md", "wt") as file:
        file.write(dataString)


if __name__ == "__main__":
    main()