from typing import List
from cycle_sort import cycle_sort
from cal_class import Cal
import json
import random as _rand
import time

def main():
    for i in range(700, 1500, 100):
        run_test_case(i)

def run_test_case(size: int):
    times = []
    for i in range(5):
        data = gen_test_set(size)
        start = time.time()
        cycle_sort(data)
        times.append(time.time() - start)

    lines = ["|{a}|{b}|\n".format(a = size, b = x) for x in times]

    with open("test_cycle_sort_{a}.md".format(a = size), "wt") as file:
        file.write("|Size|Time|\n|-|-|\n")
        file.writelines(lines)

def gen_test_set(size: int):
    with open("test_cal_data.json", "r") as file:
        data = json.load(file)
        months = data["months"]
        year_range = (data["years"]["min"], data["years"]["max"])
        day_range = (data["days"]["min"], data["days"]["max"])

    output = []
    for i in range(size):
        year = _rand.randint(year_range[0], year_range[1])
        day = _rand.randint(day_range[0], day_range[1])
        month = months[_rand.randint(0, len(months) - 1)]
        output.append(Cal(month, day, year))
    
    return output

if __name__ == "__main__":
    main()