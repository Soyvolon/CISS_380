# the program should also have Course class. Course should have two attributes a 
# name and an ArraySet (from part 1) of students registered for the course.
# The constructor for the Course class should create a Course object with a
# name and empty set of students. The Course class should have methods to add
# a student and to drop a student. When a student is added to a class its test 
# score is assigned value None. Write method to assign a test score to a particular
# student and a method to compute and return the average test grade for the entire
# curse. If, there is at least one student with score None the method should raise a
# ValueError.

from array_set import ArraySet
from student import Student

class Course(object):
    def __init__(self, courseName):
        self.courseName = courseName
        self.students = ArraySet()

    def add_student(self, firstName: str, lastName: str, score: int = None) -> None:
        """Adds a new student to the Course.

        Args:
            firstName (str): The first name of the student.
            lastName (str): The last name of the student.
            score (int, optional): The test score of the student. Defaults to None.
        """
        s = Student(firstName, lastName, score)
        self.students.add(s)

    def drop_student(self, firstName: str, lastName: str) -> bool:
        """Removes a student from the course.

        Args:
            firstName (str): First name of the student to remove.
            lastName (str): Last name of the student to remove.

        Returns:
            bool: Returns True if the student was removed, False if the student was not found.
        """
        try:
            self.students.remove(Student(firstName, lastName))
            return True
        except:
            return False

    def get_student(self, firstName: str, lastName: str) -> Student:
        """ Gets the student with the requested first and last name.

        Args:
            firstName (str): First name of the student.
            lastName (str): Last name of the student.

        Returns:
            Student: The student requested. Will return None if no
            student is found.
        """
        test = Student(firstName, lastName)
        for x in self.students:
            if x == test:
                return x
        return None

    def set_test_score(self, firstName: str, lastName: str, score: int) -> None:
        """ Sets the test score for a student. If the student does not exist, they are 
        created.

        Args:
            firstName (str): First name of the student.
            lastName (str): Last name of the student.
            score (int): Test score of the student.
        """
        s = self.get_student(firstName, lastName)
        if isinstance(s, Student):
            s.set_score(score)
        else:
            self.add_student(firstName, lastName, score)

    def get_average_test_scores(self) -> float:
        """Gets the average test score for the Course.

        Raises:
            ValueError: If a single students test score is None, a ValueError
            will be raised.

        Returns:
            float: The average test score.
        """
        avg = 0.0
        first = True
        for x in self.students:
            if x.score:
                avg += x.score
                if not first:
                    avg /= 2
                first = False
            else:
                raise ValueError("The score for {} is None".format(x.get_full_name()))
        return avg

    def __iter__(self):
        return iter(self.students)