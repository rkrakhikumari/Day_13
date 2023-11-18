stages =['''
 +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''','''
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
  |   |
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
      |
      |
      |
      |
=========''', '''        
         ''']


import random
word_list = ["rakhi","choudhary","rakhichoudhary"]
choosen_word = random.choice(word_list)
word_length = len(choosen_word)

lives = 6

print(f"the solution is {choosen_word}")

# create blanks
display = []
for _ in range(word_length):
    display += "_"

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = choosen_word[position]
        print(f"Current position: {position}\n Current letter:{letter}\n guessed letter: {guess} ")
        if letter == guess:
            display[position] = letter
    print(display)

    if guess not in choosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Loose!")
    
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You Win")
    
    print(stages[lives])

