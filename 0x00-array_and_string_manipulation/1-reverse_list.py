#!/usr/bin/python3


import unittest


def reverse_list(list_of_chars):
    """ Takes a list of characters and reverses the letters in place."""

    # Reverse the input list of chars in place
    len_list = len(list_of_chars)
    last_index = len_list - 1
    for index in range(int(len_list / 2)):
        list_of_chars[index], list_of_chars[last_index] = list_of_chars[last_index],\
        list_of_chars[index]
        last_index -= 1



















# Tests

class Test(unittest.TestCase):

    def test_empty_string(self):
        list_of_chars = []
        reverse_list(list_of_chars)
        expected = []
        self.assertEqual(list_of_chars, expected)

    def test_single_character_string(self):
        list_of_chars = ['A']
        reverse_list(list_of_chars)
        expected = ['A']
        self.assertEqual(list_of_chars, expected)

    def test_longer_string(self):
        list_of_chars = ['A', 'B', 'C', 'D', 'E']
        reverse_list(list_of_chars)
        expected = ['E', 'D', 'C', 'B', 'A']
        self.assertEqual(list_of_chars, expected)


unittest.main(verbosity=2)
