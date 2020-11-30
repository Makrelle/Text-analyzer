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
garpike and stingray are also present.'''
]
ODDELOVAC = "-" * 40
print(ODDELOVAC)

# 1. intro
print("Welcome to the app. Please log in: ")

# 2. entering username and password
username = input("USERNAME: ")
password = input("PASSWORD: ")

# 3. checking username and password
users_and_passwords = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

while username not in users_and_passwords\
        or password not in users_and_passwords.values()\
        or password != users_and_passwords[username]:
    print("Wrong username or password. Try again: ")
    username = input("USERNAME: ")
    password = input("PASSWORD: ")
print(ODDELOVAC)

# 4. selecting text
print("We have 3 texts to be analyzed.")
text_number = input("Enter a number btw. 1 and 3 to select: ")

while not text_number.isnumeric()\
        or int(text_number) < 1\
        or int(text_number) > 3:
    print("Wrong input")
    text_number = input("Enter a number btw. 1 and 3 to select: ")
print(ODDELOVAC)

text = TEXTS[int(text_number) - 1]

# 5. statistics
words = text.split()

# number of words in total
total_words = len(words)
print(f"There are {total_words} words in the selected text.")

# number of words starting with capital letter
title_count = 0
for word in words:
    if word.istitle():
        title_count += 1

print(f"There are {title_count} titlecase words.")

# number of uppercase words
upper_count = 0
for word in words:
    if word.isupper():
        upper_count += 1
print(f"There are {upper_count} uppercase words.")

# number of lowercase words
lower_count = 0
for word in words:
    if word.islower():
        lower_count += + 1
print(f"There are {lower_count} lowercase words.")

# number of numeric-only words (e.g. 100, not 100N)
numeric_count = 0
for word in words:
    if word.isnumeric():
        numeric_count += 1
print(f"There are {numeric_count} numeric strings.")
print(ODDELOVAC)

# 6. bar chart of frequencies of word lengths
clean_words = []
for word in words:
    clean_word = word.strip(",.:'")
    clean_words.append(clean_word)

frequency = dict()
while clean_words:
    clean_word = clean_words.pop(0)
    if len(clean_word) not in frequency:
        frequency[len(clean_word)] = [clean_word]
    else:
        frequency[len(clean_word)].append(clean_word)

words_lengths = sorted(frequency.keys())

for number in words_lengths:
    print(number, "*" * len(frequency[number]), len(frequency[number]))

# 7. sum of all numeric "words"
sum_of_num = 0
for word in words:
    if word.isnumeric():
        sum_of_num += int(word)
print(ODDELOVAC)
print(f"If we summed all the numbers in this text we would get: {float(sum_of_num)}")
print(ODDELOVAC)
