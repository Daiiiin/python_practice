import random

# generate random word
# number of lives = 5
# no of blank lines == no of letters in words
# player guess a letter
# make list of blank lines, no_of_blank_lines == to length of random word - 1
# if guess is in word replace blank line on the proper index
# if guess is not in word NO_OF_LIVES - 1


def generate_word():
    with open("../text_files/hangman_words.txt", "r") as fl:
        content = fl.readlines()
        rand = random.randint(1, len(content))
        word = content[rand]
        fl.close()

    return word


def generate_blank_lines(ai_word):
    word_len = len(ai_word)
    blank_lines = []
    for _ in range(word_len - 1):
        blank_lines.append("_")

    return blank_lines


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

    return idx_of_letter, lives


def main(lives):
    user_word = ""
    gen_word = generate_word()
    print(gen_word)
    blank_word = generate_blank_lines(gen_word)

    while lives != 0 or gen_word != user_word:
        # print blank lines and user lives
        print("Lives: " + str(lives))
        # concatenate list to check if word is formed
        user_word = ''.join(blank_word)
        print(user_word)

        # user inputted guess
        guess = user_guess()

        # finding letter in word
        idx_list, lives = find_letter_from_word(guess, gen_word, lives)
        # print(idx_list, lives)

        # if letter found, change blank line/s to letter
        if len(idx_list) == 0:
            print(f"Your guess {guess} not found in word.")
            lives -= 1
        else:
            for i in range(len(idx_list)):
                blank_word[idx_list[i]] = guess

        # print("User: " + user_word)
        # print("Length user: " + str(len(user_word)))
        # print("AI: " + gen_word)
        # print("Length AI: " + str(len(gen_word)))


no_of_lives = 5
main(no_of_lives)

# word2 = ''.join(var_nam)
