# exam example
# two files are used to hide a secret code, write a program able
# to extract the secret code

# opening the files
file_rec = open("ApplePieRecipe.txt","r")
file_key = open("keyCode.txt","r")

# the encoded message is saved in this string
message = ""

for line in file_key:
    message += line.strip().lower()

# only the "Instructions" part of the recipe file is used to find the hidden letters
instructions_words = []
save = False

# the Instruction section is only saved
for line in file_rec:
    if "Instructions" in line:
        save = True
    if save:
        line = line.strip().lower()
        instructions_words.extend(line.split())

# in this string the hidden code is saved
decoded_mssg = ""

# for any letter in the encoded message, the words containing the letter are found
for letter in message:
    if letter.isalpha():
        for word in instructions_words:
            # if the letter is not the first one in the word and the word is more than 3
            # letter long, the first letter in the word is taken
            if letter in word[1:] and len(word)>3:
                decoded_mssg += word[0].lower()
    else:
        decoded_mssg += " "

# printing the secret code
print(decoded_mssg)

# files closing
file_key.close()
file_rec.close()
