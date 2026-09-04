# handling CSV..
import csv

from student import Student


def read_csv_file(file_path):
    with open(file_path, mode="r") as csv_file:
        csv_records = list(csv.reader(csv_file))
        # for record in csv_records:
        #     print(record)
        return csv_records[1:]


def convert_csv_to_student_object(student_record):
    return Student(
        sid=int(student_record[0]),
        name=student_record[1],
        dept=student_record[2],
        sem=student_record[3],
        marks=[int(score) for score in student_record[4:]],
    )


def write_csv_file(file_path, student_records):
    with open(file_path, mode="w") as output_file:
        csv_writer = csv.writer(output_file)

        csv_writer.writerow(
            [
                "Student_ID",
                "Name",
                "Department",
                "Semester",
                "Subject1",
                "Subject2",
                "Subject3",
            ]
        )

        for student_record in student_records:
            csv_writer.writerow(
                [
                    student_record.sid,
                    student_record.name,
                    student_record
                ]
            )

