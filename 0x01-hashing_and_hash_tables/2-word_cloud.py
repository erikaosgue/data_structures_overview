#!/usr/bin/python3

import unittest


class WordCloudData(object):
    """
    Takes a long string and builds word cloud data
    in the instance dictionary
    """

    def __init__(self, input_string):
        """
            Adds a cloud data dict to the instance,
            base on the input_string
        """
        self.words_to_counts = {}
        self.split_and_populate_words(input_string)

    def split_and_populate_words(self, input_string):
        """
        Split and cleanr the words from input_string
        getting only alpha characters or allow_chars
        """
        start_word = 0
        len_word = 0
        allow_chars = {'\''}

        for i, char in enumerate(input_string):

            # if we reached the last char in the string, we need to
            # make sure we add the last word into the dict
            if i == len(input_string) - 1 or i == "\u2014":

                if char.isalpha():
                    len_word += 1

                # if last word is just one char (Perhaps is not something very
                # common) we make sure to add it
                if len_word == 1:
                    start_word = i

                # if there is a last word still pending to add to the dict, we
                # add it here
                if len_word > 0:
                    word = input_string[start_word: start_word + len_word]
                    print("Last_word:", word)
                    self.add_word_to_dict(word)

            # if there is a dash between two words,
            # that is a valid char in the word
            # Example: mille-feuille
            elif i > 0 and char == "-" and input_string[i-1].isalpha()\
                    and input_string[i+1].isalpha():
                len_word += 1

            # if char is a letter or a valid char, we include it in the word
            elif char.isalpha() or char in allow_chars:
                if len_word == 0:
                    start_word = i
                len_word += 1

            # if there is a valid word to add and we reached
            # a not valid char such as space or dot
            # we add the word to the dict
            elif len_word > 0:
                word = input_string[start_word: start_word + len_word]
                self.add_word_to_dict(word)
                len_word = 0

    def add_word_to_dict(self, word):
        """
        Add a word to the dict if doesn't exist,
        or incremente its value base on:
        * If the word already exists
        * If the word in the dict is capitalize and the input is not
        * If The word in the dict is lowercase and the input is not
        """

        # if the word already exist in the dict
        # we increment 1 the value
        if word in self.words_to_counts:
            self.words_to_counts[word] += 1

        # if the word in the dict is capitalize
        # we add the new word lower case, with the value of the
        # capitalize word plus 1
        # and delete the old capitalize word
        elif word.capitalize() in self.words_to_counts:
            self.words_to_counts[word] = self.words_to_counts[
                word.capitalize()] + 1
            del self.words_to_counts[word.capitalize()]

        # if the word in the dict is lower case but the input
        # is capitalize, we just increment the value of the word by 1
        elif word.lower() in self.words_to_counts:
            self.words_to_counts[word] += 1

        # if the word doen't exist in the dict, we add the new word
        else:
            self.words_to_counts[word] = 1

# Tests

# There are lots of valid solutions for this one. You
# might have to edit some of these tests if you made
# different design decisions in your solution.


class Test(unittest.TestCase):

    def test_simple_sentence(self):
        input = 'I like cake'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {'I': 1, 'like': 1, 'cake': 1}
        self.assertEqual(actual, expected)

    def test_longer_sentence(self):
        input = 'Chocolate cake for dinner and pound cake for dessert'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {
            'and': 1,
            'pound': 1,
            'for': 2,
            'dessert': 1,
            'Chocolate': 1,
            'dinner': 1,
            'cake': 2,
        }
        self.assertEqual(actual, expected)

    def test_punctuation(self):
        input = 'Strawberry short cake? Yum!'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {'cake': 1, 'Strawberry': 1, 'short': 1, 'Yum': 1}
        self.assertEqual(actual, expected)

    def test_hyphenated_words(self):
        input = 'Dessert - mille-feuille cake'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {'cake': 1, 'Dessert': 1, 'mille-feuille': 1}
        self.assertEqual(actual, expected)

    def test_ellipses_between_words(self):
        input = 'Mmm...mmm...decisions...decisions'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {'mmm': 2, 'decisions': 2}
        self.assertEqual(actual, expected)

    def test_apostrophes(self):
        input = "Allie's Bakery: Sasha's Cakes"

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {"Bakery": 1, "Cakes": 1, "Allie's": 1, "Sasha's": 1}
        self.assertEqual(actual, expected)

    def test_last_word_one_letter(self):
        input = "Allie's Bakery: Sasha's Cakes t"

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {
            "Bakery": 1, "Cakes": 1, "Allie's": 1, "Sasha's": 1, "t": 1}
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
