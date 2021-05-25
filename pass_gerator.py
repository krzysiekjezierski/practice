import sys
password =[]
characters_left = -1

password_length = int(input('Jak długie ma być to hasło? '))


if password_length < 5:
    print("Hasło musi mieć przynajmniej 5 znaków, spóbuj ponownie jeszcze raz :) ")
    sys.exit(0)
else:
    characters_left = password_length

lowercase_letters = int(input('Ile małych liter powinno mieć hasło? ')

if lowercase_letters > characters_left:
    print('Liczba znaków przekracza liczbę wolnych znaków.')
    sys.exit(0)

uppercase_letter = int(input('Ile dużych liter powinno mieć hasło? '))
special_characters = int(input('Ile znaków specjalnych powinno mieć hasło? '))
digits = int(input('Ile cyfr powinno mieć hasło? '))