import sys

number_of_tries = 5
word = "dupa wołowa"
used_letters = []

user_word = []

def find_indexes(word, letter):
    indexes = []

    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)

    return indexes
def show_state_of_game():
    print()
    print(user_word)
    print("Pozostało prób:", number_of_tries)
    print("użyte litery", used_letters)
    print()

###

for _ in word:
    user_word.append('_')

while True:
    letter = input("Podaj literę: ")
    used_letters.append(letter)

    found_indexes = find_indexes(word, letter)

    if len(found_indexes) == 0:
        print("\nNie ma tekiej litery.")
        number_of_tries -= 1
        # print("Pozostało prób", number_of_tries)

        if number_of_tries == 0:
            print("Koniec gry, nie udało się, wisisz ;-(")
            sys.exit(0)
    else:
        for index in found_indexes:
            user_word[index] = letter
        # print(user_word)

        if "".join(user_word) == word:
            print("\nBrawo, udało Ci się tym razem ;-)")
            sys.exit(0)

    # print('Użyte litery:',used_letters)

    show_state_of_game()