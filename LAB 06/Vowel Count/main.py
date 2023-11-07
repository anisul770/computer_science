def vowel_count(text):
    vowel_set = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    count = 0
    for i in range(len(text)):
        if text[i] in vowel_set:
            count += 1
    return count


sentence = input('Type your word or sentence')
print(vowel_count(sentence))
