import random
from words import words

def create_blanks(word, guesses):
  a = []
  for i in word:
    if guesses.__contains__(i):
      a.append(i)
    else:
      a.append("_")
  res = {"res": " ".join(a), "won": word == "".join(a)}
  return res

def game():
  word = random.choice(words).upper()
  tries = 6
  guesses = []

  print("Welcome to Hangman Game!\n")
  while tries > 0:
    res = create_blanks(word, guesses)
    if res["won"] == True:
      print(f'\nWord: {word}\nCongratulations you won! \nTries Left: {tries}')
      return
    
    print(f'{display_hangman(tries)}')
    print(f'{res["res"]}')  
    guess = input("\nEnter a letter: ").upper()
    if word.__contains__(guess):
      if guesses.__contains__(guess):
        print("\nYou took that guess already\n")
      guesses.append(guess)
    else:
      tries -= 1
      print(f'\nWrong! You have {tries} tries left!\n')

  print(f'{display_hangman(tries)}')
  print(f'\nYou Lost :(\nWord: {word}')
  

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                 # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

game()