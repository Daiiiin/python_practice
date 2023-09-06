import random

# WRITING LIST
with open("../text_files/file_practice.txt", "w") as f:
    myList = ["Apple", "Orange", "Banana", "Grapes", "Watermelon"]
    for x in myList:
        f.write(x + "\n")
    f.close()

rand = random.randint(1, len(myList))

# with open("../text_files/file_practice.txt", "r") as f:
#     content = f.readlines()
#     print(content)
#     print(type(content))
#     f.close()

with open("../text_files/file_practice.txt", "r") as f:
    line = f.readlines()[rand - 1]
    print(line)
    print("length: " + str(len(line)))
    # print(rand)
    # print(myList)
    # print(type(line))
    f.close()

