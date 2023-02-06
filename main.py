from hangman_words import word_list
from hangman_art import logo, stages
import random

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# Testing code
# print(f'Don't tell anybody but the answer is {chosen_word}.')

print(logo)

#Create blank display
display = []
for _ in range(word_length):
  display += "_"

#Game loop, True = end
while not end_of_game:
  guess = input("Guess a letter: ").lower()

  past_guess = []
  if guess in past_guess:
    print("You've already guessed this word")
  else:
    past_guess.append(guess)
      
  #Check guessed letter
  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter

  #Check if user is wrong
  if guess not in chosen_word:
    lives -= 1
    print(f"{guess} is not in the word")
    if lives == 0:
      end_of_game = True
      print("You lose!")

  #Join all the elements in the list and convert to string
  print(f"{' '.join(display)}")

  #Check if user guessed all the letters
  if "_" not in display:
    end_of_game = True
    print("You win!")
  #Print lives remaining visual
  print(stages[lives])
  