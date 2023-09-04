import random


def generate_word():
    with open("../text_files/hangman_words.txt", "r") as fl:
        content = fl.readlines()
        rand = random.randint(1, len(content))
        word = content[rand]
        fl.close()

    return word

# def hangman_game():


generate_word()
