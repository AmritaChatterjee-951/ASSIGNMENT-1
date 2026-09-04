# For handling Json..
import json

from student import Student


def read_json_file(file_path):
    json_content = None

    with open(file_path, "r") as json_file:
        json_content = json.load(json_file)

    return json_content


def convert_json_to_student_object(student_data):
    subject_marks = [
        student_data["marks"]["subject1"],
        student_data["marks"]["subject2"],
        student_data["marks"]["subject3"],
    ]

    return Student(
        student_data["sid"],
        student_data["name"],
        student_data["dept"],
        student_data["sem"],
        subject_marks
    )


def write_json_file(file_path, student_list):

    json_records = [
        {
            "sid": student_record.sid,
            "name": student_record.name,
            "dept": student_record.dept,
            "sem": student_record.sem,
            "marks": {
                "subject1": student_record.marks[0],
                "subject2": student_record.marks[1],
                "subject3": student_record.marks[2],
            },
        }
        for student_record in student_list
    ]

    with open(file_path, "w") as json_file:
        json.dump(json_records, json_file, indent=4)


# Test this file individually
if __name__ == "__main__":
    print(read_json_file("students.json"))
