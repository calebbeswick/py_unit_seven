def four_letters(phrase):
    split_list = phrase.split()
    for x in range(len(split_list)):
        if len(split_list[x]) == 4:
            split_list[x] = "#$%@"
    list_two = " ".join(split_list)
    return list_two





def bubble_sort(words):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'j', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'y', 'z']
    alphabetical = False
    while alphabetical != True:
        for x in range(len(words)):
            for i in range(len(words)-1)
                if words[i] > words[i+1]
                temp1 = words[i]
                temp2 = words[i + 1]
                words[i] = temp2
                words[i+1] = temp1
if __name__ == '__main__':
    four_letters("have a nice day")
    bubble_sort()
