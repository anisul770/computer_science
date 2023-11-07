def classes(file):
    try:
        with open(file) as infile:
            line = infile.readline().strip()
            class_list = []
            while line != '':
                class_list.append(line)
                line = infile.readline().strip()
    except IOError:
        print(f'{file} does not exist')
        exit()

    return class_list


def student_grade(class_list, student):
    for i in range(len(class_list)):
        try:
            with open(f'{class_list[i]}.txt', 'r') as infile:
                line = infile.readline().strip()
                id_dict = {}
                while line != '':
                    tmp_list = line.split(' ')
                    id_dict[tmp_list[0]] = tmp_list[1]
                    line = infile.readline().strip()
                if student in id_dict:
                    print(f'{class_list[i]} {id_dict[student]}')
                else:
                    print(f'{student} do not have {class_list[i]}')
        except IOError:
            print(f'{class_list[i]} dose not exist')


def main():
    student_id = input("Enter student ID: ")
    student_grade(classes('Classes.txt'), student_id)


if __name__ == '__main__':
    main()
