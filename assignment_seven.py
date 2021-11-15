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
        num = random.randint(0, 1)
        num2 = random.randint(0, 1)
        if case == "y":
            if numbers == "y":
                if num2 == 1:
                   character = random.randint(0, 9)
                elif num2 == 0:
                    character = random.choice(list_of_letters)
                    if num == 0:
                        character = character[:1].upper()
                    elif num == 1:
                        character = character[:1].upper()
                        character = character[:1].lower()

        elif case == "n":
            if numbers == "y":
                if num2 == 1:
                   character = random.randint(0, 9)
                else:
                    character = random.choice(list_of_letters)
                    character = character[:1].upper()
                    character = character[:1].lower()

        else:
            character = random.choice(list_of_letters)
            character = character[:1].upper()
            character = character[:1].lower()
        character = str(character)
        empty_list.append(character)
        empty_list = "".join(empty_list)
    print(empty_list)




random_word()
random_password()

