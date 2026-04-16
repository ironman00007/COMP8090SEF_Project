class Manager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student_id):
        self.students = [s for s in self.students if s.get_student_id() != student_id]

    def display_students(self):
        for s in self.students:
            print(s.get_info())
