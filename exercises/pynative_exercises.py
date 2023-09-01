def sum_of_curr_prev():
    for i in range(10):
        print("Current: " + str(i) + " | Previous: " + str(i - 1) + " | Sum: " + str(i + i - 1))


def char_at_even_index():
    word = input("Enter a word: ")
    for i in range(0, len(word) - 1, 2):
        print(word[i])


print("Sum of current and previous number:")
sum_of_curr_prev()

print("Print characters from a string that are present at an even index number:")
char_at_even_index()
