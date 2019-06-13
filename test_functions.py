"""Test for my functions."""

from functions import choose_language

def choose_language_test():
    assert choose_language('english') == 'english'

def choose_language_test_german():
    assert select_language('german') == 'german'

def choose_language_test_others():
    assert select_language('french') == ValueError

