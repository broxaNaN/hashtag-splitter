# Original code from: https://stackoverflow.com/questions/195010/how-can-i-split-multiple-joined-words.
# Adapted code to return list of tokens and their ranges.

import re
from collections import Counter

def split_hashtag(text):
    probs, lasts = [1.0], [0]
    text = text.replace(text[0], '')
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
        test_dict = {}
        sample = re.search(words[index], text)
        sample_tuple = sample.span()
        test_dict['token'] = words[index]
        test_dict['start'] = sample_tuple[0] + 1
        test_dict['end'] = sample_tuple[1]
        final_list.append(test_dict)
    return final_list

def word_prob(word): return dictionary[word] / total
def words(text): return re.findall('[a-z]+', text.lower()) 
dictionary = Counter(words(open('big.txt').read()))
max_word_length = max(map(len, dictionary))
total = float(sum(dictionary.values()))

print(split_hashtag('#orasulbucuresti'))