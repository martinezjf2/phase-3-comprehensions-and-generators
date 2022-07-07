#!/usr/bin/env python3

def return_evens(num_list):
    list_comprehension = [number for number in num_list if number % 2 == 0]
    return list_comprehension

def make_exclamation(sentence_list):
    list_comprehension = [sentence + "!" for sentence in sentence_list]
    return list_comprehension
    pass