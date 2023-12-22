import re
import os

file = open('./DAY_01/INPUT_01.txt', 'r')
lines = list(map(lambda x: re.sub(r'\n', '', x), file.readlines()))

total = 0
for line in lines: 
    cleaned = re.sub(r'[^\d]+', '', line)
    n = cleaned[0] + cleaned[-1]  
    total += int(n)

print("SOLUTION PT 1 {}".format(total))

num_word_lookup = {
    "one": "1", 
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


def replace_number_words(line):
    res = ''
    i = 0
    while i < len(line):
        if line[i] in ["1","2","3","4","5","6","7","8","9"]:
            res+=line[i]
        else:
            three_letter = num_word_lookup.get(line[i:i+3])
            four_letter = num_word_lookup.get(line[i:i+4])
            five_letter = num_word_lookup.get(line[i:i+5])
            if three_letter:
                res += three_letter      
            elif four_letter:
                res += four_letter
            elif five_letter:
                res += five_letter
        i += 1
    return res

total = 0
for line in lines:
    cleaned = replace_number_words(line)
    n = cleaned[0] + cleaned[-1] 
    total += int(n)

print("SOLUTION PT 2 {}".format(total))
