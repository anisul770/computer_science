
def main():
   stop = False
   while not stop:
      play()
      yn = input("Play another game? (y/n): ")
      if yn.strip().lower().startswith('n'):
            stop = True


def play():
   word = list()
   last = input('Insert a word: ').strip().lower()
   word.append(last)

   valid_game = True

   while valid_game:
      new = input("Insert a new word: ").strip().lower()
      if new == '*':
         valid_game = False
         print('The user wants to quit')
      elif len(new)<2 or new[:2] != last[-2:]:
         valid_game = False
         print('The world is not valid')
      elif new in word:
         valid_game = False
         print('The word has already been said')
      else:
         word.append(new)
      last = new


main()
