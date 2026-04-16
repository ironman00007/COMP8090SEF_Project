from person import Person

class Student(Person):
    def __init__(self, student_id, name):
        super().__init__(name)
        self.__student_id = student_id
        self.__courses = []

    def get_student_id(self):
        return self.__student_id

    def add_course(self, course):
        self.__courses.append(course)

    def get_info(self):
        return f"Student ID: {self.__student_id}, Name: {self.name}"
