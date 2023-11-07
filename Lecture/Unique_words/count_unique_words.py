# This program counts and print the number of unique words in a file
#
def main():
    inFile = open("marys_lamp.txt", "r")
    # all the file lines are read in a single instruction.
    # a list called lines is created
    lines = inFile.readlines()
    # a new list is created to save all the words in the file
    new_list = []
    for line in lines:
        line = line.strip()
        tmp_l = line.split()
        for word in tmp_l:
            # any word in the line is cleaned and saved in the new list
            new_list.append(word.rstrip(".,;:'").upper())

    # printing the resulting words in the list
    print(f"size of list: {len(new_list)}")
    print(sorted(new_list))

    # printing the resulting words in the list
    set_of_words = set(new_list)
    print(f"size of set: {len(set_of_words)}")
    print(sorted(set_of_words))

    inFile.close()





main()
