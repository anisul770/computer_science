def read_classes(class_file_name):

    try:
        with open(class_file_name) as class_file:

            classes = class_file.readline()
            for i in range(len(classes)):
                classes[i] = classes[i].strip()

            return classes

    except IOError:
        print("The file doesn't exist")
        exit(-1)


def read_grades_in_class(student_id,class_name):

    class_file_name = f'{class_name}.txt'

    try:
        with open(class_file_name) as class_file:

            lines = class_file.readline()

            for line in lines:
                if student_id in line:
                    grade = line.replace(student_id, '').strip()

                    return grade
        raise ValueError(f'student {student_id} not {class_name}')
    except IOError:
        print("The file doesn't exist")
        exit(-1)


def main():
    student_id = input('Input a student ID')

    class_list = read_classes('Classes.txt')

    grade_dict = dict()

    for class_name in class_list:
        try:
            grade = read_grades_in_class(student_id,class_name)
            grade_dict[class_name] = grade
        except ValueError as value_exception:
            print(f'WARNING {value_exception}')
    for key, value in grade_dict.items():
        print(f'{key}:\t{value}')


main()
