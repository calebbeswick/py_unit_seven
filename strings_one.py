def half_slice(word):
    string_two = ""
    length = len(word)
    first_number = length // 2
    second_number = length - first_number
    string_two = string_two + word[first_number:]
    string_two = string_two + word[:first_number]
    return string_two

def upper_lower(word):
    print(word.upper())
    print(word.lower())
    length = len(word)
    for letter in word:
        print(letter)


def no_first_last(str):
    no_first_or_last = print(str[1:-1])
    return no_first_or_last

def longest(phrase):
    pass


def title_case(sentence):
    pass

def main():
    half_slice("cookie")
    upper_lower("caleb")
    no_first_last("hello")

main()