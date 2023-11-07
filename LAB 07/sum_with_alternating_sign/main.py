
def sign_list(line):
    list_ = []
    for i in range(len(line)):
        if line[i].isdigit() is False:
            list_.append(line[i])
    return list_


def integer_list(line):
    list_ = []
    count = 0
    for i in range(len(line)):
        if not line[i].isdigit():
            list_.append(line[i-count:i])
            count = 0
        elif line[i].isdigit():
            count += 1
            if i == len(line)-1:
                list_.append(line[i-count+1:i+count])

    return list_


def summation(sign, integer):
    sum_ = int(integer[0])
    j = 0
    for i in range(1, len(integer)):
        if sign[j] == "+":
            sum_ = sum_ + int(integer[i])
        elif sign[j] == '-':
            sum_ = sum_ - int(integer[i])
        j += 1

    return sum_


def main():
    line = input("Enter sequence: ")
    line.strip()
    sign = sign_list(line)
    integer = integer_list(line)
    total = summation(sign, integer)
    print(f'Summation of the sequence :{total}')


if __name__ == '__main__':
    main()
