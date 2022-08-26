# Implemented during a research stage at ICIA. 
# Viterbi algorithm from https://stackoverflow.com/questions/195010/how-can-i-split-multiple-joined-words, 
# adapted to the Romanian language. 

import re
from collections import Counter
from arguments import getArguments

args = getArguments()

def replace_diacritice(s):
    s = s.replace("ă","a").replace("î","i").replace("â","a").replace("ș","s").replace("ț","t")
    if args.lower == "Yes":
        return s
    if args.lower == "No":
        return s.replace("Ă","A").replace("Î","I").replace("Â","A").replace("Ș","S").replace("Ț","T")

def upper_letters(hashtag):
    list = []
    for index in range(len(hashtag)):
        if hashtag[index].isupper():
            list.append(index)
    return list

def split_hashtag ():
    probs, lasts = [1.0], [0]
    ok = False
    text = args.hashtag
    text = text.replace(text[0], '')
    if args.lower == "No":
        found_index = upper_letters(text)
    text = text.lower()
    if args.remove_diacritics == "Yes":
        text = replace_diacritice(text)
    last_position = 0
    if text[0] == '#':
        text = text.replace(text[0], '')
        ok = True
    final_list = []
    for i in range(1, len(text) + 1):
        prob_k, k = max((probs[j] * word_prob(text[j:i]), j)
                        for j in range(max(0, i - max_word_length), i))
        probs.append(prob_k)
        lasts.append(k)
    words = []
    i = len(text)
    while 0 < i:
        words.append(text[lasts[i]:i])
        i = lasts[i]
    words.reverse()
    for index in range(len(words)):
        word_dict = {}
        sample = re.search(words[index], text[last_position:])
        sample_tuple = sample.span()
        found_word = words[index]
        if args.lower == "No":
            if ok == True:
                for index_2 in range(len(found_index)):
                    found_word = found_word.replace(found_word[found_index[index_2] - 1],
                                                    found_word[found_index[index_2] - 1].upper())
            else:
                for index_2 in range(len(found_index)):
                    found_word = found_word.replace(found_word[found_index[index_2]],
                                                    found_word[found_index[index_2]].upper())
        word_dict['token'] = found_word
        if ok == True:
            word_dict['start'] = sample_tuple[0] + 1
            word_dict['end'] = sample_tuple[1]
        else:
            word_dict['start'] = sample_tuple[0]
            word_dict['end'] = sample_tuple[1] - 1
        word_dict['start'] += last_position
        word_dict['end'] += last_position
        last_position = word_dict['end']
        final_list.append(word_dict)
    return final_list

dictionary = {}
file = args.frequency_file
fileLines = file.read().split('\n')

for index in range(len(fileLines) - 1):
    key, value = fileLines[index].split('\t')
    value = int(value)
    dictionary[key] = value

dictionary = Counter(dictionary)

def word_prob(word): 
    return dictionary[word] / total

max_word_length = max(map(len, dictionary))
total = float(sum(dictionary.values()))

print(split_hashtag())
