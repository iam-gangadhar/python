import random

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

word_list = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

choosen_word = random.choice(word_list)

guess_list = []
for _ in range(len(choosen_word)):
    guess_list.append('_')

print("soultion word: ",choosen_word)
game_on = True
lives = 0
while game_on:

    guess = input('Enter a Letter to guess..').lower()
    position = 0
    if guess in choosen_word:
        for i in choosen_word:
            if guess == i:
                guess_list[position] = i
            position += 1
    else:
        print(HANGMANPICS[lives])
        lives += 1

    print(guess_list)
    if '_' not in guess_list:
        game_on = False
        print("You won..")
    if lives > 6:
        print("Game Over")
        game_on = False

