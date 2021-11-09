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
    no_first_or_last = str[1:-1]
    return no_first_or_last

def longest(phrase):

    words = phrase.split(" ")
    longest = ""
    for word in words:

        if len(word) >= len(longest):
            longest = word
    return(longest)







def title_case(sentence):
    words = sentence.split(" ")
    capitals = ""
    list_two = []
    for word in words:
        s = word[0]
        s = s.upper()
        x = s + word[1:]
        list_two.append(x)
    capitals = " ".join(list_two)
    return capitals



def main():
    half_slice("cookie")
    upper_lower("caleb")
    no_first_last("hello")
    title_case("The quick brown fox jumped lazy the lazy dog")

main()