def count_words(string):
    x = string.split(' ')
    for i in range(len(x)):
        if '' in x:
            x.remove('')
    print(len(x))


string = input('Type your sentence:')
count_words(string)
