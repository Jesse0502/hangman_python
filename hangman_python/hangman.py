import os
import random
from words import words

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'): 
        command = 'cls'
    os.system(command)

def create_blanks(word, guesses):
  a = []
  for i in word:
    if i in guesses:
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
    clearConsole()
    print(f'\t\tTries Left: {tries}')
    print(f'{display_hangman(tries)}')
    print(f'{res["res"]}')  
    guess = input("\nEnter a letter: ").upper()
    if guess in word:
      if guess in guesses:
        print("\nYou took that guess already\n")
      guesses.append(guess)
    else:
      tries -= 1
      print(f'\nWrong! You have {tries} tries left!\n')

  print(f'{display_hangman(tries)}')
  print(f'\nYou Lost :(\nWord: {word}')
  

def display_hangman(tries):
    stages = [  
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
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