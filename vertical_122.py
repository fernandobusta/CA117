#!/usr/bin/env python3

import sys

#get the vertical letters
def convert(words):
    vert_words = []
    for w in words[0]:
        #set the number of strings in vert_list = len(str in words)
        vert_words.append('')
    #iterate through every word to create new strings inside vert
    try:
        for w in words:
            i = 0
            #we want to get a single ch of the word
            while i < len(w):
                #append the character to the new string
                vert_words[i] += w[i]
                i += 1
    except IndexError:
        #error we might encounter:
        #1 -> additional str of length < str[0]
        return None
    return vert_words


#try:
#sort the vertical letters alphabetically
def alph_sort(vert_words):
    #this is the list containing the words sorted and LOWER CASE
    s = sorted([n.lower() for n in vert_words])
    alph_words = []
    #iterating through every word in s=sorted_alph_lower_list
    for w in s:
        i = 0
        #find word s[i] in vert list
        while w != vert_words[i].lower() and i < len(vert_words):
            i += 1
        #add the word to list alph
        alph_words.append(vert_words[i])
        #remove the word from vert list
        vert_words.pop(i)
    return alph_words
#except IndexError:
#   i = 1
#   #see if the error is due to an extra line of different length
#   while len(alph_words[i - 1]) == len(alph_words[i]) and i < len(alph_words):
#      i += 1
#   if len


def build_output(alph_words):
    #check if there is an error: due to not equal length strings
    try:
        return '\n'.join(alph_words)
    except TypeError:
        return 'The elements of the list are not of equal lentgth'


words = [w.strip() for w in sys.stdin]
converted = convert(words)
#print(converted)
if converted is not None:
    alph_words = (alph_sort(converted))
    #print(alph_words)
    final_output = convert(alph_words)
    print(build_output(final_output))
else:
    print('The elements of the list are not of equal length')
