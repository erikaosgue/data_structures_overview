#!/usr/bin/python3

import unittest


def reverse_words(message):
    """Takes a message as a list of characters and reverses the order of the words in place."""
    
    full_list = []
    temp_list = []
    for char in message:
        if char == " ":
            temp_list.insert(0, " ")
            full_list = temp_list + full_list
            temp_list = []
        else:
            temp_list.append(char)
    full_list = temp_list + full_list
    message[:] = full_list[:]















# Tests

class Test(unittest.TestCase):

    def test_one_word(self):
        message = list('vault')
        reverse_words(message)
        expected = list('vault')
        self.assertEqual(message, expected)

    def test_two_words(self):
        message = list('thief cake')
        reverse_words(message)
        expected = list('cake thief')
        self.assertEqual(message, expected)

    def test_three_words(self):
        message = list('one full get')
        reverse_words(message)
        expected = list('get full one')
        self.assertEqual(message, expected)

    def test_multiple_words_same_length(self):
        message = list('rat the ate cat the')
        reverse_words(message)
        expected = list('the cat ate the rat')
        self.assertEqual(message, expected)

    def test_multiple_words_different_lengths(self):
        message = list('yummy is cake bundt chocolate')
        reverse_words(message)
        expected = list('chocolate bundt cake is yummy')
        self.assertEqual(message, expected)

    def test_empty_string(self):
        message = list('')
        reverse_words(message)
        expected = list('')
        self.assertEqual(message, expected)


unittest.main(verbosity=2)
