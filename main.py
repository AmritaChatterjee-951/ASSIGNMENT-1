```python
import argparse
import os

from manager import StudentManager


def main():
    command_parser = argparse.ArgumentParser(
        description="Student Record Management System"
    )

    command_parser.add_argument("--file", help="input file path")
    command_parser.add_argument(
        "--format",
        choices=["txt", "csv", "json"],
        help="file format"
    )

    command_arguments = command_parser.parse_args()

    record_manager = StudentManager()

    if command_arguments.file and os.path.exists(command_arguments.file):
        print(f"Loading records from {command_arguments.file}...")

        record_manager.load_from_file(
            command_arguments.file,
            command_arguments.format
        )

        print(
            f"Loaded {len(record_manager.student)} student(s)."
        )

    else:
        print(
            f"File '{command_arguments.file}' not found. "
            "Starting with an empty student records database."
        )

    while True:
        print("\n=========== Student Record Management System ===========")
        print("1. Add a New Student")
        print("2. Display All Students")
        print("3. Search for a Student by ID")
        print("4. Remove a Student by ID")
        print("5. Calculate Total & Average Marks")
        print("6. Save Records to File")
        print("7. Display All Students including their Results")
        print("8. Exit")
        print("-" * 100)

        menu_choice = input("Enter choice (1-8): ").strip()
        print("\n")

        match menu_choice:

            case "1":
                try:
                    registration_id = int(
                        input("Enter Student ID (integer): ").strip()
                    )

                    if any(
                        record.sid == registration_id
                        for record in record_manager.student
                    ):
                        print("Error: Student with this ID already exists.")
                        continue

                    student_full_name = input(
                        "Enter Student Name: "
                    ).strip()

                    student_department = input(
                        "Enter Department: "
                    ).strip()

                    student_semester = input(
                        "Enter Semester: "
                    ).strip()

                    examination_marks = []

                    for subject_index in range(3):
                        subject_mark = int(
                            input(
                                f"Enter Marks for Subject {subject_index + 1}: "
                            ).strip()
                        )

                        examination_marks.append(subject_mark)

                    record_manager.add_student(
                        registration_id,
                        student_full_name,
                        student_department,
                        student_semester,
                        examination_marks
                    )

                    print(
                        f"Student '{student_full_name}' added successfully."
                    )

                except ValueError:
                    print(
                        "Invalid input. Please enter numbers for ID and marks."
                    )

            case "2":
                if not record_manager.student:
                    print("No student records available.")
                else:
                    record_manager.display_all_student()

            case "3":
                try:
                    registration_id = int(
                        input("Enter Student ID to search: ").strip()
                    )

                    found_student = record_manager.search_student(
                        registration_id
                    )

                    if found_student:
                        print("\n--- Student Found ---")
                        found_student.display_student_details()

                except ValueError:
                    print(
                        "Invalid input. Student ID must be an integer."
                    )

            case "4":
                try:
                    registration_id = int(
                        input("Enter Student ID to remove: ").strip()
                    )

                    record_manager.remove_student(registration_id)

                except ValueError:
                    print(
                        "Invalid input. Student ID must be an integer."
                    )

            case "5":
                try:
                    registration_id = int(
                        input(
                            "Enter Student ID to calculate marks: "
                        ).strip()
                    )

                    found_student = record_manager.search_student(
                        registration_id
                    )

                    if found_student:
                        found_student.display_student_details()

                except ValueError:
                    print(
                        "Invalid input. Student ID must be an integer."
                    )

            case "6":
                output_file = input(
                    "Enter file name/path to save:"
                )

                output_format = input(
                    "Save in which format? (json,csv,txt):"
                )

                print(
                    f"Saving records to {output_file} "
                    f"in {output_format} format..."
                )

                save_status = record_manager.save_to_file(
                    output_file,
                    output_format
                )

                print(
                    "\nRecords saved successfully.\n"
                    if save_status
                    else "\nFailed to save records.\n"
                )

            case "7":
                print("Print All details of Students........")
                record_manager.display_all_student(
                    only_data=False
                )

            case "8":
                print("Exiting program!.........")
                break

            case _:
                print(
                    "Invalid choice. Please enter a number between 1 and 7."
                )


if __name__ == "__main__":
    main()
```
