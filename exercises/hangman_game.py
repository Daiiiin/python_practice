import random


def generate_word():
    with open("../text_files/hangman_words.txt", "r") as fl:
        content = fl.readlines()

    word = random.choice(content)

    return word


def generate_blank_lines(ai_word):
    word_len = len(ai_word)
    blank_lines = []
    for _ in range(word_len):
        blank_lines.append("_")

    return blank_lines


def find_letter_from_word(letter, word, lives):
    idx_of_letter = []
    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                idx_of_letter.append(i)

    return idx_of_letter, lives


def main(lives):
    # random generated word
    ai_word = generate_word().strip()
    blank_word = generate_blank_lines(ai_word)

    while lives != 0:
        # print user lives
        print("\nLives: " + str(lives))

        # concatenate list to check if word is formed
        user_word = ''.join(blank_word)

        # print lines
        print(user_word)

        # check if user has won
        if user_word == ai_word:
            print("\nYou Win!")
            break

        # user inputted guess
        guess = input("Guess a letter: ").lower()

        # finding letter in word
        idx_list, lives = find_letter_from_word(guess, ai_word, lives)
        # print(idx_list, lives)

        # if letter found, change blank line/s to letter
        if len(idx_list) == 0:
            print(f"Your guess {guess} not found in word.")
            lives -= 1
        else:
            for i in range(len(idx_list)):
                blank_word[idx_list[i]] = guess
    else:
        print(f"\nThe word was {ai_word}.\nYou Lose!")


no_of_lives = 5
main(no_of_lives)

# word2 = ''.join(var_nam)
