"""
Rudimentary text prediction algorithm. 'Learns from' text sources and generates random body of text in that style.
"""
from typing import TextIO
from random import choice


# Task 1
def make_dictionary(filename: str) -> dict[str, list[str]]:
    """
    Return a dictionary where the keys are words in <filename> and the value
    for a key is the list of words that were found to follow the key.
    """
    with open(filename) as f:
        list_of_words = f.read().split()
    
    # construct dictionary
    sex = {}
    for i in range(len(list_of_words) -1):
        p = list_of_words[i]
        sex[p] = []


    for i in range(len(list_of_words)-1):
        k, v = list_of_words[i], list_of_words[i+1]
        sex[k].append(v)

    with open('word_dict_temp.txt', 'w') as g:
        for i in sex:
            g.write(f"{i}: {sex[i]}\n")
    
    return sex


# Task 2
def mimic_text(word_dict: dict[str, list[str]], num_words: int) -> str:
    """
    Based on the word patterns in <word_dict>, return a string with
    <num_words> words that mimics the text.
    """

    outstring = "The "
    c_last_word = "The"

    for i in range(num_words):
        
        added_word = choice(word_dict[c_last_word]) # choose random element
        outstring += f"{added_word} "

        c_last_word = added_word

    return outstring



if __name__ == '__main__':

    word_d = make_dictionary('alice.txt')  # try changing text files!
    print(f"\n{mimic_text(word_d, 100)}\n")          # test different <num_words> lengths!
