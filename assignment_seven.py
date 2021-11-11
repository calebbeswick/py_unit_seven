#
#
#

import random

text = open("english.txt", "r")
list_of_words = text.readlines()
text.close()


# words is if it is random or three words
#length_of_password is how many characters in the password
#type_of_pas
#

def random_word():
    word = []
    rand_word1 = random.choice(list_of_words)
    rand_word2 = random.choice(list_of_words)
    rand_word3 = random.choice(list_of_words)
    word = str(rand_word1) + str(rand_word3) + str(rand_word2)
    print(word)

random_word()



