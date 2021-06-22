def verify_student_information(id: int, name: str, semester: int, homework_avg: int):
    if str(id)[0]=='0' or not name.isalpha() or semester<1 or homework_avg not in range(51,101):
        return False

def calculate_final_grade(id:int,homework_avg:int):
    return (id%100+homework_avg)//2


def write_to_output_path(students_dict:dict,output_path: str):
    file_output = open(output_path,"w")
    for student_id in sorted(students_dict):
        (name, semester, homework_avg) = students_dict[student_id]
        file_output.write(F"{student_id}, {homework_avg}, {calculate_final_grade(student_id,homework_avg)}\n")
    file_output.close()

def final_grade(input_path: str, output_path: str) -> int:
    file_input = open(input_path, "r")
    students_dict = {}
    for line in file_input:
        line_data = line.split(",")
        (id, name, semester, homework_avg) = line_data
        if verify_student_information(id,name,semester,homework_avg):
            students_dict[id]=[name,semester,homework_avg]
    write_to_output_path(students_dict,output_path)
    file_input.close()
