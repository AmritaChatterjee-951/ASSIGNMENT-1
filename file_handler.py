from student import Student


def read_from_file(file_location):
    """Assuming in comma separated format"""

    records = []

    with open(file_location) as input_file:

        while True:
            text_line = input_file.readline()

            if not text_line:
                break

            fields = text_line.strip().split(",")

            records.append(
                Student(
                    int(fields[0]),
                    fields[1],
                    fields[2],
                    fields[3],
                    [score for score in map(int, fields[4:])]
                )
            )

    return records


def write_txt_file(file_location, student_records):
    """Just put the console print out things as rowise format into file
    So, this is not compatible with `read_from_file()` method
    """

    with open(file_location, "w") as output_file:

        for student_record in student_records:
            output_file.writelines(
                student_record.display_student_row() + "\n"
            )


# test this file only.......
if __name__ == "__main__":
    print("Testing write_txt_file:")

    student_records = read_from_file("students.txt")

    # write_txt_file("./data/test_students2.txt", student_records)

    for student_record in student_records:
        print(student_record)

