def censor():
    try:
        with open('Bad.txt', 'r') as file:
            with open('Censored.txt', 'w') as cencsored:
                line = file.readline().strip()
                bad = ['sex', 'drugs', 'python']
                while line != "":
                    tmp = line.split(' ')
                    for i in bad:
                        if i in tmp:
                            index = tmp.index(i)
                            tmp[index] = '*'*len(i)
                    cencsored.write(f"{' '.join(tmp)}\n")
                    line = file.readline().strip()
    except IOError:
        print('File not found')


def main():
    censor()


main()
