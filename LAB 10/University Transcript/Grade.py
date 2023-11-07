def classes(file):
    try:
        with open(file, "r") as class_file:
            class_name = class_file.readline().strip()
            class_list = []
            while class_name != '':
                class_list.append(class_name)
                class_name = class_file.readline().strip()
    except IOError:
        print(f"{file} doesn't exits")

    return class_list


def grade(student_id, class_list):
    for i in range(len(class_list)):
        try:
            with open(f'{class_list[i]}.txt', 'r') as file:
                line = file.readline().strip()
                id_dict = {}
                while line != '':
                    line = line.split(' ')
                    id_dict[line[0]] = line[1]
                    line = file.readline().strip()
                if student_id in id_dict:
                    print(f'{class_list[i]} {id_dict[student_id]}')
                else:
                    print(f"{class_list[i]} doesn't contain {student_id}")

        except IOError:
            print(f"{class_list[i]} doesn't exits")


def main():
    student_id = input('Enter student ID: ')
    class_list = classes('Classes.txt')
    grade(student_id, class_list)


if __name__ == '__main__':
    main()
