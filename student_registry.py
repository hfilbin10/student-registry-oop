class Student:
    def __init__(self, name, age = 13, grade = "12th"):
        self._name = name
        self._age = age
        self._grade = grade

    @property
    def get_name(self):
        return self._name
    
    @property
    def get_age(self):
        return self._age
    
    @property
    def get_grade(self):
        return self._grade
    
    @get_name.setter
    def set_name(self, new_name):
        if isinstance(new_name, str) and len(new_name) >= 3:
        # new_name.isalpha() and new_name.istitle() and len(new_name) >= 3:
            self._name = new_name.title()
            # for char in new_name:
            #     if (char.isnumeric() or char.isalpha()):
            #         self.name = new_name

    @get_age.setter
    def set_age(self, new_age):
        if type(new_age) == int and new_age > 11 and new_age < 18:
            self._age = new_age
    
    @get_grade.setter
    def set_grade(self, new_grade):
        if int(new_grade[:-2]) in range(9, 13) and new_grade.endswith("th"):
            self._grade = new_grade

    def __str__(self):
        return f"{self.get_name} is {self.get_age} years old & in the {self.get_grade} grade."

    def advance(self, grade):
        print(f"{self._name} has advanced to the {grade} grade.")

    def study(self, subject):
        print(f"{self._name} is studying {subject}.")

student_one = Student("Stud", 23, "10th")
halsey = Student("Halsey", 33, "16th")
josh = Student("Josh", 28, "19th")

print(halsey)
print(josh)
# print(student_one)

# student_one.advance("14th")
# student_one.study("history")

# print(student_one._name)
# student_one.set_name = "hal"
# print(student_one._name)

# print(student_one._age)
# student_one.set_age = 18
# print(student_one._age)

# print(student_one._grade)
# student_one.set_grade = "13th"
# print(student_one._grade)