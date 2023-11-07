def get_playfair_couple(playfair_matrix, sequence):

    sequence = sequence.replace('j', 'i')

    row_1 = col_1 = None
    row_2 = col_2 = None

    for row in range(len(playfair_matrix)):
        for col in range(len(playfair_matrix)):

            if playfair_matrix[row][col] == sequence[0]:
                row_1 = row
                col_1 = col

            if playfair_matrix[row][col] == sequence[1]:
                row_2 = row
                col_2 = col
    if row_1 == row_2 or col_1 == col_2:
        cipherd_character_1 = sequence[1]
        cipherd_character_2 = sequence[0]
    else:
        cipherd_character_1 = playfair_matrix[row_1][col_2]
        cipherd_character_2 = playfair_matrix[row_2][col_1]

    cipherd_sequence = cipherd_character_1 + cipherd_character_2

    return  cipherd_sequence


def build_playfair_matrix(keyword):

    alphabet = 'abcdefghiklmnopqrstuvwxyz'

    keyword = keyword.lower().strip()

    keyword = keyword.replace('j', 'i')

    unique_character = ''
    for character in keyword:
        if character not in unique_character:
            unique_character += character

    for character in unique_character:
        alphabet.replace(character, '')

    playfair_string = unique_character +alphabet

    playfair_matrix = list()

    for row in range(5):
        row_list = ['']*5
        for col in range(5):
            row_list[col] = playfair_string[row*5 + col]
        playfair_matrix.append(row_list)

    return playfair_matrix


def main():

    keyword = input('Enter a keyword')

    playfair_matrix = build_playfair_matrix(keyword)

    for row in playfair_matrix:
        for col in row:
            print(col, end='\t')
        print()

    file_name = 'input/10.2.3 Playfair cipher/input.txt'
    file = open(file_name, "r")
    input_text = file.read()
    file.close()

    preprocessed_text = ''

    for char in input_text:
        if char.isalpha():
            preprocessed_text += char.lower()

    if len(preprocessed_text)%2 == 1:
        preprocessed_text += 'z'

    ciphered_text = ""

    for index_pair in range(0,len(preprocessed_text),2):
        pair = preprocessed_text[index_pair:index_pair + 2]
        ciphered_pair = get_playfair_couple(playfair_matrix, pair)
        ciphered_text += ciphered_pair

    print(ciphered_text)

    deciphered_text = ""

    for index_pair in range(0,len(ciphered_text),2):
        pair = preprocessed_text[index_pair:index_pair + 2]
        deciphered_pair = get_playfair_couple(playfair_matrix, pair)
        deciphered_text += deciphered_pair

    print(deciphered_text)
''' 
    same as previous one
    with open(file_name, 'r') as file:
    input_text = file.read()
'''

main()
