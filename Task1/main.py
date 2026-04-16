from student import Student
from manager import Manager
from utils import get_student_names, sort_students

def main():
    manager = Manager()

    s1 = Student(1, "YUE XIAOBO")
    s2 = Student(2, "Alice")

    manager.add_student(s1)
    manager.add_student(s2)

    print("All students:")
    manager.display_students()

    print("\nStudent names:")
    print(get_student_names(manager.students))

    print("\nSorted students:")
    sorted_students = sort_students(manager.students)
    for s in sorted_students:
        print(f"{s.get_student_id()} - {s.name}")

if __name__ == "__main__":
    main()
