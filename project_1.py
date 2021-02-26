# my first project - text analyzer

'''
author =
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.''']

SEPARATOR = "-" * 40
print(SEPARATOR)

# intro
print("Welcome to the app. Please log in: ")

# enter username and password
username = input("USERNAME: ")
password = input("PASSWORD: ")

# check username and password
users_and_passwords = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

while username not in users_and_passwords\
        or password != users_and_passwords[username]:
    print("Wrong username or password. Try again: ")
    username = input("USERNAME: ")
    password = input("PASSWORD: ")

print(SEPARATOR)

# select text
print("We have 3 texts to be analyzed.")
text_number = input("Enter a number btw. 1 and 3 to select: ")

while not text_number.isnumeric()\
        or int(text_number) < 1\
        or int(text_number) > 3:
    print("Wrong input")
    text_number = input("Enter a number btw. 1 and 3 to select: ")

print(SEPARATOR)

text = TEXTS[int(text_number) - 1]

# statistics
words = text.split()
total_words = len(words)
title_count = 0
upper_count = 0
lower_count = 0
numeric_words = []
clean_words = []
frequency = dict()

for word in words:
    if word.istitle():
        title_count += 1
    if word.isupper():
        upper_count += 1
    if word.islower():
        lower_count += 1
    if word.isnumeric():
        numeric_words.append(float(word))
    clean_word = word.strip(",.:'")
    if len(clean_word) not in frequency:
        frequency[len(clean_word)] = 1
    else:
        frequency[len(clean_word)] += 1

print(f"""There are {total_words} words in the selected text.
There are {title_count} titlecase words.
There are {upper_count} uppercase words.
There are {lower_count} lowercase words.
There are {len(numeric_words)} numeric strings.""")

print(SEPARATOR)

# bar chart of frequencies of word lengths
words_lengths = sorted(frequency.keys())
for number in words_lengths:
    print(number, "*" * frequency[number], frequency[number])

print(SEPARATOR)
print(f"""If we summed all the numbers in this text
we would get: {float(sum(numeric_words))}""")
print(SEPARATOR)

