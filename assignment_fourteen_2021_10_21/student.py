# 2. Write Python program that will allow a professor to maintain a list of
# students for a given course. The program should contain a basic Student
# class with attributes for the first name, last name and test score. Write
# the basic __init__, __str__ methods and get and set methods for the attributes.

class Student(object):
    def __init__(self, firstName, lastName, score = None):
        self.firstName = firstName
        self.lastName = lastName
        self.score = score

    def get_first_name(self):
        return self.firstName

    def set_first_name(self, firstName):
        self.firstname = firstName
    
    def get_last_name(self):
        return self.lastName
        
    def set_last_name(self, lastName):
        self.lastname = lastName

    def get_score(self):
        return self.score
        
    def set_score(self, score):
        self.score = score

    def get_full_name(self):
        return self.firstName + " " + self.lastName

    def __str__(self):
        return "{ \"first_name\": \"{}\", \"last_name\": \"{}\", \"score\": \"{}\" }"\
            .format(self.firstName, self.lastName, self.score)

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Student):
            return False

        return o.firstName.lower() == self.firstName.lower() \
            and o.lastName.lower() == self.lastName.lower()