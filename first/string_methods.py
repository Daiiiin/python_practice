name = "Matthew Dave Desabelle"

# length
print("length: " + str(len(name)))
# find
print("find s: " + str(name.find("s")))
# capitalize the first letter
word1 = "hello"
print("capitalize: " + word1.capitalize())
# upper, converts string to uppercase
print("upper: " + word1.upper())
# lower, converts string to lowercase
word2 = "MORNING"
print("lower: " + word2.lower())
# isdigit, return true if string is digit, otherwise false
word3 = "11"
print("isdigit Case 1: " + str(word2.isdigit()))
print("isdigit Case 2: " + str(word3.isdigit()))
# isalpha, if alphabet = true, else = false, if there is white space = false
print("isalpha Case 1: " + str(word2.isalpha()))
print("isalpha Case 2: " + str(name.isalpha()))
# count
print("Count (number of e): " + str(name.count("e")))
# replace
print("Replace all e with g: " + name.replace("e", "g"))
# print a string multiple times
print(word1 * 5)
