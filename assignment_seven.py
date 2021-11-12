#
#
#

import random

text = open("english.txt", "r")
list_of_words = text.readlines()
text.close()



alpha = open("Alphabet", "r")
list_of_letters = alpha.readlines()
text.close()


# words is if it is random or three words
#length_of_password is how many characters in the password
#type_of_pas
#

def random_word():
    word = []
    rand_word1 = random.choice(list_of_words)
    return rand_word1


def random_password():
    characters = int(input("Please enter the amount of characters of your password "))
    case = input("Would you like capital letters? (y/n) ")
    numbers = input("Would you like numbers? (y/n) ")
    symbols = input("Would you like symbols? (y/n) ")
    empty_list = []
    for letters in range(characters):
        num = random.randrange(0, 1)
        num2 = random.randrange(0, 3)
        if case == "y" and num == 1:
            if numbers == "y" and num2 == 3:
                character = random.randint(0, 9)
            elif num2 == 0:
                character = random.choice(list_of_letters)
                character = character.capitalize()
            elif num2 == 1:
                character = random.choice(list_of_letters)
        else:
            character = random.choice(list_of_letters)
        empty_list.append(character)
    print(empty_list)



random_word()
random_password()

