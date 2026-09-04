# Student class

class Student:
    def __init__(self, student_id: int, name: str, department: str,
                 semester: str, subject_marks: list):

        self.student_id = student_id
        self.name = name
        self.department = department
        self.semester = semester
        self.subject_marks = subject_marks

    def calculate_total(self):
        return sum(self.subject_marks)

    def calculate_average(self):
        return sum(self.subject_marks) / len(self.subject_marks)

    def update_marks(self, new_marks):
        self.subject_marks = new_marks

    def update_name(self, new_name):
        self.name = new_name

    def update_semester(self, new_semester):
        self.semester = new_semester

    def get_result(self):
        for mark in self.subject_marks:
            if mark < 33:
                return "Fail"

        return "Pass"

    def display_student_details(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Semester: {self.semester}")
        print(f"Marks: {self.subject_marks}")
        print(f"Total: {self.calculate_total()}")
        print(f"Average: {self.calculate_average():.2f}")
        print(f"Result: {self.get_result()}")

    def display_student_row(self, only_data=True):
        marks_text = ",".join(map(str, self.subject_marks))

        student_row = (
            f"{self.student_id:<10}"
            f"{self.name:<12}"
            f"{self.department:<12}"
            f"{self.semester:<10}"
            f"{marks_text:<15}"
        )

        if not only_data:
            total_marks = self.calculate_total()
            average_marks = self.calculate_average()
            result = self.get_result()

            return (
                f"{student_row}"
                f"{total_marks:<10.2f}"
                f"{average_marks:<10.2f}"
                f"{result:<8}"
            )

        return student_row


# Test the Student class

if __name__ == "__main__":

    student_one = Student(
        101,
        "Rahul",
        "Computer Science",
        "   1st",
        [78, 62, 89]
    )

    print(student_one.display_student_row())

    student_two = Student(
        102,
        "Priya",
        "Computer Science",
        "   1st",
        [91, 87, 94]
    )

    print(student_two.display_student_row())

    student_one = Student(
        103,
        "Amit",
        "Mathematics",
        "       1st    ",
        [65, 71, 68]
    )

    print(student_one.display_student_row())


    print("\nStudent Details:")
    student_one.display_student_details()


