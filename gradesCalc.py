#### PART 1 ####


def verify_student_information(id: str, name: str, semester: int, homework_avg: int):
    """
    Verifies student information is valid by designated set of rules
    """
    if id[0] == '0' or len(id) != 8 or not name.isalpha() or semester < 1 or homework_avg \
            not in range(51, 101):
        return False
    return True


def calculate_final_grade(id: int, homework_avg: int):
    """
    Calculates final grades based on id and homework
    """
    return (id % 100 + homework_avg) // 2


def write_to_output_path_and_calculate_final_grade(students_dict: dict, output_path: str):
    """
    Writes to output file and calculates semester final average
    """
    final_grade_list = []
    file_output = open(output_path, "w")
    for student_id in sorted(students_dict):
        (name, semester, homework_avg) = students_dict[student_id]
        student_final_grade = calculate_final_grade(student_id, homework_avg)
        file_output.write(F"{student_id}, {homework_avg}, {student_final_grade}\n")
        final_grade_list.append(student_final_grade)
    file_output.close()
    if final_grade_list:
        return sum(final_grade_list) // len(final_grade_list)
    return 0


def unpack_data_field_line(line: str):
    """
    Unpacks line and formats it
    """
    line_data = line.split(",")
    (id, name, semester, homework_avg) = line_data
    return id.replace(" ", ""), name.replace(" ", ""), int(semester), int(homework_avg)


# final_grade: Calculates the final grade for each student, and writes the output (while eliminating illegal
# rows from the input file) into the file in `output_path`. Returns the average of the grades.
#   input_path: Path to the file that contains the input
#   output_path: Path to the file that will contain the output
def final_grade(input_path: str, output_path: str) -> int:
    file_input = open(input_path, "r")
    students_dict = {}
    for line in file_input:
        id, name, semester, homework_avg = unpack_data_field_line(line)
        if verify_student_information(id, name, semester, homework_avg):
            students_dict[int(id)] = [name, semester, homework_avg]
    finale_grade_average = write_to_output_path_and_calculate_final_grade(students_dict, output_path)
    file_input.close()
    return finale_grade_average


#### PART 2 ####
# check_strings: Checks if `s1` can be constructed from `s2`'s characters.
#   s1: The string that we want to check if it can be constructed
#   s2: The string that we want to construct s1 from
def check_strings(s1: str, s2: str) -> bool:
    s2_dict = {}
    s1 = s1.lower()
    s2 = s2.lower()
    for char in s2:
        if char in s2_dict:
            s2_dict[char] += 1
        else:
            s2_dict[char] = 1
    for char in s1:
        if not s2_dict.get(char):
            return False
        s2_dict[char] -= 1
    return True
