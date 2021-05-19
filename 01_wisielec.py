number_of_tries = 5
word = "kamil"
used_letters = []

used_word = []

def find_indexes(word, letter):
    indexes = []

    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)

    return indexes

###

for _ in word:
    used_word.append('_')

while True:
    letter = input("Podaj literę: ")
    used_letters.append(letter)

    print(find_indexes(word, letter))

    print('Użyte litery:',used_letters)