from dataclasses import dataclass


@dataclass
class Student:
    student_id: int
    name: str
    marks: int


class StudentModel:
    def __init__(self):
        self.students = []

    def add_student(self, student: Student) -> None:
        self.students.append(student)

    def get_all_students(self) -> list[Student]:
        return self.students


def student_list_view(model: StudentModel) -> list[dict]:
    return [
        {"id": student.student_id, "name": student.name, "marks": student.marks}
        for student in model.get_all_students()
    ]


if __name__ == "__main__":
    model = StudentModel()
    model.add_student(Student(1, "Rahul", 88))
    model.add_student(Student(2, "Sara", 92))
    print(student_list_view(model))
