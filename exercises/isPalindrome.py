def is_palindrome(s):
    length = len(s)
    end = length - 1
    for i in range(0, int(length/2)):
        if s[i] == s[end]:
            end -= 1
            continue
        else:
            print("The word " + s + " is NOT a palindrome")
            break
    else:
        print("The word " + s + "is a palindrome")


while True:
    word = input("Enter a word: ")
    if not word.isalpha():
        print("Please enter a word.")
    else:
        word = word.lower()
        is_palindrome(word)
        break
