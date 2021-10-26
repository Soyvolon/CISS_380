# 1. A set is an unordered collection with the same interface as a bag.
# However, the items in a set are unique, whereas a bag can contain
# duplicate items. Define a new class named ArraySet that implements
# an array-based set type. The add method simply ignores the item if it’s already in the set. 

# 2. Write Python program that will allow a professor to maintain a list of
# students for a given course. The program should contain a basic Student
# class with attributes for the first name, last name and test score. Write
# the basic __init__, __str__ methods and get and set methods for the attributes.
# the program should also have Course class. Course should have two attributes a 
# name and an ArraySet (from part 1) of students registered for the course.
# The constructor for the Course class should create a Course object with a
# name and empty set of students. The Course class should have methods to add
# a student and to drop a student. When a student is added to a class its test 
# score is assigned value None. Write method to assign a test score to a particular
# student and a method to compute and return the average test grade for the entire
# curse. If, there is at least one student with score None the method should raise a
# ValueError. Finally, write the main program that will allow professor to manage a course.
# Please, notice that you need to write an actual main program that user can interact with
# not just tester for your classes. 

from student import Student
from course import Course

def cls() -> None:
    # print("\033[H\033[J", end="")
    print("\n"*5)
    print("-"*10)
    print("\n"*5)

def print_student(index: int, student: Student) -> None:
    score = 0.0
    if student.score != None:
        score = student.score
    print("%5s] %-45s %-15s %.2f" % (index, student.get_first_name(), student.get_last_name(), score))

def print_header(data: str, clr: bool = True) -> None:
    if clr:
        cls()
    print("%45s" % (data))

def print_alert(alert):
    if alert != "":
        print()
        print(alert)
        print()

def print_menu(header: str, options, alert: str = "") -> None:
    print_header(header)
    print_alert(alert)
    for x in range(1, len(options) + 1):
        print("[%-5s] %-20s" % (x, options[x - 1]))

def print_student_header():
    print("%5s] %-45s %-15s %15s" % ("Index", "First Name", "Last Name", "Test Score"))

def print_all_students(col: Course):
    print_student_header()
    c = 1
    for x in col:
        print_student(c, x)
        c += 1

def prompt(header: str, prompts, alert: str = "", clr: bool = True):
    print_header(header, clr)
    print_alert(alert)
    data = []
    for x in range(1, len(prompts) + 1):
        data.append(input("[%-5s] %s: " % (x, prompts[x-1])))
    return data

def student_prompt(header: str, prompts, col: Course, alert: str = ""):
    print_header(header)
    print_alert(alert)
    print_all_students(col)
    print()
    data = []
    for x in range(1, len(prompts) + 1):
        data.append(input("[%-5s] %s: " % (x, prompts[x-1])))
    return data

def single_student_prompt(header: str, prompts, student: Student, alert: str = ""):
    print_header(header)
    print_alert(alert)
    print_student_header()
    print_student(1, student)
    print()
    data = []
    for x in range(1, len(prompts) + 1):
        data.append(input("[%-5s] %s: " % (x, prompts[x-1])))
    return data

def main():
    print_menu("Course Manager", ["Enter a Course Name to continue:"])

    cname = input()

    course = Course(cname)
    main_menu = ["Add Student",\
                "Drop Student",\
                "Update Test Score",\
                "Get Student",\
                "List Students",\
                "Get Course Average",\
                "Exit"]

    print_menu("Managing {}".format(course.courseName), main_menu)
    data = input()    
    while data != "7":
        alert = ""
        if data == "1":
            alert = add_student(course)
        elif data == "2":
            alert = remove_student(course)
        elif data == "3":
            alert = update_test_score(course)
        elif data == "4":
            alert = get_student(course)
        elif data == "5":
            alert = list_all_students(course)
        elif data == "6":
            alert = get_course_average(course)
        else:
            alert = "A value between 1 and 7 must be entered."

        print_menu("Managing {}".format(course.courseName), main_menu, alert)
        data = input()

    print("Shutting Down Course Manager...")

def add_student(course) -> str:
    prompts = ["Enter Student First Name",\
                "Enter Student Last Name"]

    data = prompt("Add Student", prompts)

    course.add_student(data[0], data[1])

    return "Added the student: {} {}".format(data[0], data[1])

def remove_student(course) -> str:
    prompts = ["Enter Student First Name",\
                "Enter Student Last Name"]
    data = student_prompt("Drop Student", prompts, course)

    res = course.drop_student(data[0], data[1])

    if res:
        return "Dropped {} {} from the course.".format(data[0], data[1])
    else:
        return "Unable to drop a non-existent student."

def update_test_score(course) -> str:
    prompts = ["Enter Student First Name",\
                "Enter Student Last Name",\
                "Enter New Test Score"]
    data = student_prompt("Update Test Score", prompts, course)

    score = None
    try:
        score = float(data[2])
    except:
        return "Test score was not a number."

    course.set_test_score(data[0], data[1], score)

    return "Updated the test score for {} {} to {:.2f}".format(data[0], data[1], score)

def get_student(course) -> str:
    prompts = ["Enter Student First Name",\
                "Enter Student Last Name"]

    data = prompt("Add Student", prompts)

    res = course.get_student(data[0], data[1])

    if res == None:
        return "No student was found."
    else:
        print_student(0, res)
        prompt("Found Student", ["Press enter to return to main menu"], "", False)
        return ""

def list_all_students(course) -> str:
    print_all_students(course)
    prompt("Student Display", ["Press enter to return to main menu"], "", False)
    return ""

def get_course_average(course) -> str:
    prompt("Course Average: {}".format(course.get_average_test_scores()), \
        ["Press enter to return to main menu"], "", False)
    return ""

if __name__ == "__main__":
    main()