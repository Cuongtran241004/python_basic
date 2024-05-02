import random
# word_list is a fake data to test this program
from words import word_list, hint
# import logo
from art import logo, stages

# Using random library to create a random word from the word_list

chosen_word = random.choice(word_list)
hint = hint[chosen_word]
word_length = len(chosen_word)
end_of_game = False
lives = 6

# Print the logo
print(logo)

# Creating a list of blanks to display to the user
display = []

for letter in range(word_length):
    display += "_"

while not end_of_game:
    print(hint)
    # Asking the user to guess a letter
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f">>> Already guessed {guess}")

    for i in range(word_length):
        letter = chosen_word[i]
        if letter == guess:
            display[i] = letter

    if guess not in chosen_word:
        print(">>> You lost 1 live!")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win!")

    # print stages
    print(stages[lives])
