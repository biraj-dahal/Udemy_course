import random
print("""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
""")
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      | 
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

do_you_want_to_play = input("Do you want to play? \nEnter Y for Yes, and N for No.\n")
while do_you_want_to_play == "Y":
    lives_lost = 0
    words_list = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
            'coyote crow deer dog donkey duck eagle ferret fox frog goat '
            'goose hawk lion lizard llama mole monkey moose mouse mule newt '
            'otter owl panda parrot pigeon python rabbit ram rat raven '
            'rhino salmon seal shark sheep skunk sloth snake spider '
            'stork swan tiger toad trout turkey turtle weasel whale wolf '
            'wombat zebra ').split()
    word_to_play = random.choice(words_list)
    blank_word = ['_'for _ in range(len(word_to_play))]
    seen = set()
    while lives_lost < 6 and blank_word.count('_') != 0:
        print('\nWORD:   ',"  ".join(blank_word), '\n')
        print(HANGMANPICS[lives_lost])
        word_guessed = input("\nGuess a letter: ").lower()
        if word_guessed in seen:
            print("No lives lost. You have already guessed this word before. Try another word.")
        elif word_guessed in word_to_play:
            for index in range(len(word_to_play)):
                if word_to_play[index] == word_guessed:
                    blank_word[index] = word_guessed
            seen.add(word_guessed)
        else:
            print(f"Sorry, the word {word_guessed} is not in the secret word.")
            lives_lost += 1
            seen.add(word_guessed)
    if blank_word.count('_') == 0:
        print('\nWORD:   ',"  ".join(blank_word), '\n')
        print("You won!")
        do_you_want_to_play = input("Do you want to play again? \nEnter Y for Yes, and N for No.\n")
    else:
        print(HANGMANPICS[-1])
        print("\nSo soryy, but you lost. The secret WORD was ", word_to_play )
        do_you_want_to_play = input("Do you want to play again? \nEnter Y for Yes, and N for No.\n")


    
