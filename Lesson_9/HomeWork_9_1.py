import os

# file = open('famous phrase.txt', 'r')
# print(file.read(5))
# print(file.tell())
# file.close()
# print(os.getcwd())
# file_path ='C:/Users/bonda/PycharmProjects/python_Begin/Lesson_9/famous phrase.txt'
# file = open(file_path, 'r')
# print(file.read())

new_file = "famous_phrase.txt"
with open('Files/famous phrase.txt', 'r', encoding='utf-8') as my_file:
    with open('Files/famous phrase_rev.txt', 'w') as phrase_rev:
        for line in my_file:
            phrase_rev.write(line)



