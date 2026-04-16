def get_student_names(students):
    return [s.name for s in students]

def sort_students(students):
    return sorted(students, key=lambda s: s.get_student_id())
