# hashtag-splitter

The code uses the Viterbi algorithm to determine the most probable sequence of words in Romanian. 
The function returns an array of all the tokens found, along with their range (start and end position).
It admits a string parameter. The first step is to normalize the text (transforming it into lowercase and removing the hashtag symbol). 
Using a TSV file containing words and their frequency, it calculates the aforementioned words' probabilities and when words are found, they get added to an array. 
For each word, a dictionary is created. The keys are as follows: "token", "start", "end". The values are in correspondance to each word. 
All of the dictionaries get appended to the previously mentioned array that gets returned by the algorithm.
