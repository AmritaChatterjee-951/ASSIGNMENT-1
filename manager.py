from csv_handler import *
from file_handler import *
from json_handler import *
from student import Student


# Student Manager class
class StudentManager:

    def __init__(self):
        self.student_list: list[Student] = []

    def add_student(self, student_id: int, student_name: str,
                    department: str, semester: str, subject_marks: list):

        self.student_list.append(
            Student(
                student_id,
                student_name,
                department,
                semester,
                subject_marks
            )
        )

    def remove_student(self, student_id: int):

        for current_student in self.student_list:

            if current_student.student_id == student_id:

                self.student_list.remove(current_student)

                print(f"Student removed {current_student.name}")

                return self.student_list

        print("Student not found")

    def search_student(self, student_id):

        for current_student in self.student_list:

            if current_student.student_id == student_id:
                return current_student

        print("Student not found")

    def display_all_student(self, only_data=True):

        output_string = (
            f"{'SID':<3} "
            f"{'Name':<10} "
            f"{'Dept':<8} "
            f"{'Sem':<4} "
            f"{'Marks':<10}"
        )

        if not only_data:

            print(
                f"\n--- All Student Records "
                f"({len(self.student_list)}) ---"
            )

            output_string = (
                output_string +
                f" {'Total':<7} "
                f"{'Average':<7} "
                f"{'Result':<7}"
            )

        print(output_string)
        print("-" * 100)

        for current_student in self.student_list:
            print(
                current_student.display_student_row(only_data)
            )

        print("-" * 100)

    def save_to_file(self, file_name, file_format):

        if file_format == "csv":

            write_csv_file(
                file_name,
                self.student_list
            )

        elif file_format == "json":

            write_json_file(
                file_name,
                self.student_list
            )

        elif file_format == "txt":

            write_txt_file(
                file_name,
                self.student_list
            )

        else:

            print("Invalid format")
            return False

        return True

    def load_from_file(self, file_name, file_format):

        if file_format == "csv":

            file_data = read_csv_file(file_name)

            for student_data in file_data:

                self.student_list.append(
                    convert_csv_to_student_object(student_data)
                )

        elif file_format == "json":

            file_data = read_json_file(file_name)

            for student_data in file_data:

                self.student_list.append(
                    convert_json_to_student_object(student_data)
                )

        elif file_format == "txt":

            file_data = read_from_file(file_name)

            self.student_list.extend(file_data)

        else:

            print("Invalid format")
            return False

        return True


# Individually test this class file only
if __name__ == "__main__":

    manager = StudentManager()

    print("\nAdding students...")

    manager.add_student(
         101,
        "Rahul",
        "Computer Science",
        "   1st",
        [78, 62, 89]
    )

    manager.add_student(
        102,
        "Priya",
        "Computer Science",
        "   1st",
        [91, 87, 94]
    )

    manager.add_student(
        103,
        "Amit",
        "Mathematics",
        "       1st    ",
        [65, 71, 68]
    )

    manager.display_all_student()

    manager.search_student(102)

    manager.save_to_file(
        "students.csv",
        "csv"
    )

    manager.save_to_file(
        "students.json",
        "json"
    )

    manager.save_to_file(
        "students.txt",
        "txt"
    )

    manager.remove_student(102)

    manager.display_all_student()
