'''### Task 4.9
Implement a bunch of functions which receive a changeable number of strings and return next parameters:

1) characters that appear in all strings

2) characters that appear in at least one string

3) characters that appear at least in two strings

4) characters of alphabet, that were not used in any string

Note: use `string.ascii_lowercase` for list of alphabet letters
python
test_strings = ["hello", "world", "python", ]
print(test_1_1(*test_strings))
>>> ('o',)
print(test_1_2(*test_strings))
>>> ('d', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 't', 'w', 'y',)
print(test_1_3(*test_strings))
>>> ('h', 'l', 'o',)
print(test_1_4(*test_strings))
>>> ('a', 'b', 'c', 'f', 'g', 'i', 'j', 'k', 'm', 'q', 's', 'u', 'v', 'x', 'z',)'''
import functools
import string
import collections

def intersection_of_strings_set(values: list) -> set:
    '''
    Returns characters that appear in all strings.
    :param values: input list of strings
    :return: characters that appear in all strings.
    '''
    return functools.reduce(lambda a, b: a & b, [set(s) for s in values])

def intesection_of_strings_tuple(values: list) -> tuple[str]:
    '''
    Returs characters that appear in all string
    :param values: input list of strings
    :return: characters that appears in all string
    '''
    return tuple(intersection_of_strings_set(values))

def characters_in_at_least_two_strings(values: list[str]) -> tuple[str]:
    '''
    Returns characters that appears at least in two strings.
    :param values: input list of strings
    :return: Characters that appear at least in two strings.
    '''
    list_of_unique_word_chars = [''.join(set(word)) for word in values]
    char_counts = collections.Counter("".join(list_of_unique_word_chars))
    return tuple(char for char in char_counts if char_counts[char] >= 2)

def not_used_alphabets_set(values : list[str]) -> set:
    '''
    Returns characters of alphabets, that were not used in any string.
    :param values: input list of strings
    :return: characters if alphabet, that were not used in any string.
    '''
    return set(values.ascii_lowecase) - union_of_strings_set(values)

def not_used_alphabets_tuple(values : list[str]) -> tuple[str]:
    '''
    Returns characters of alphabet, that were not used in any string.
    :param values: input list of string
    :return: charactes of aplhabet, that were not used in any string.
    '''
    return tuple(not_used_alphabets_set(values))

if __name__ == '__main__':
    test_strings = ['Hello', 'world', 'python']
    assert intesection_of_strings_tuple(test_strings) == ('o')
