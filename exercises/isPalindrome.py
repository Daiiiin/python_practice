def is_palindrome(s):
    length = len(s)
    end = length - 1
    for i in range(0, int(length/2)):
        if s[i] == s[end]:
            end -= 1
            continue
        else:
            return False
    return True


check = False

while True:
    word = input("Enter a word: ")
    if not word.isalpha():
        print("Please enter a word.")
    else:
        word = word.lower()
        check = is_palindrome(word)
        break

print("The word " + word + " is a palindrome: " + str(check))
