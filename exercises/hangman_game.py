import random

# generate random word
# number of lives = 5
# no of blank lines == no of letters in words
# player guess a letter
# if guess is in word fill in blank
# if guess is not in word NO_OF_LIVES - 1


def generate_word():
    with open("../text_files/hangman_words.txt", "r") as fl:
        content = fl.readlines()
        rand = random.randint(1, len(content))
        word = content[rand]
        fl.close()

    return word


def user_guess():
    return input("Guess a letter: ").lower()


def find_letter_from_word(letter, word, lives):
    no_of_letter = 0
    idx_of_letter = []
    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                no_of_letter += 1
                idx_of_letter.append(i)
    else:
        print(f"Your guess {letter} not found in word.")
        lives -= 1

    return idx_of_letter, lives


no_of_lives = 5

# random generated word from txt file
gen_word = generate_word()
print(gen_word)

# user inputted guess
guess = user_guess()

# finding letter in word
idx_list, no_of_lives = find_letter_from_word(guess, gen_word, no_of_lives)
print(idx_list, no_of_lives)
