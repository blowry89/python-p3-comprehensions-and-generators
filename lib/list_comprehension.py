#!/usr/bin/env python3

def return_evens(num_list): # Python function called return_evens that takes a list of numbers num_list as input.
    ## Function returns a new list that contains only the even numbers from the input list.
    return [n for n in num_list if n%2 == 0] #creates a new list by iterating over each element n in the num_list and checking if it is divisible by 2.

 #Python list comprehension. A compact way to create a new list by performing a specific operation on each element of an existing list.

def make_exclamation(sentence_list):
    return [sentence + "!" for sentence in sentence_list]
# sentence + "!" concatenates each sentence with the exclamation mark.
# for sentence in sentence_list iterates over each sentence in the sentence_list. 
# The resulting expression sentence + "!" is then added to the new list.