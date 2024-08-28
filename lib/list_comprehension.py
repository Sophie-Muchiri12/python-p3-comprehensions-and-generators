#!/usr/bin/env python3

def return_evens(num_list):
    evennums = [ num for num in num_list if (num % 2 == 0)]
    return evennums
return_evens([1,2,3,4,5,6,7,8,9])

def make_exclamation(sentence_list):
    words = [word + "!" for word in sentence_list]
    return words

make_exclamation(["Hello", "I'm doing great", "Python is fun"])