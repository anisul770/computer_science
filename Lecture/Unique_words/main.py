
def main():
    inFile = open("marys_lamp.txt", "r")
    lines = inFile.readlines()
    new_list = []
    for line in lines:
        line = line.strip()
        tmp_l = line.split()
        for word in tmp_l:
            new_list.append(word.rstrip(".,;:'").upper())
    # lines = infile.readline()
    print(f"size of list : {len(new_list)}")
    print(new_list)
    set_of_words = set(new_list)
    print(f"size of list : {len(set_of_words)}")
    print(set_of_words)
    inFile.close()

main()
