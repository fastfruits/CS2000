"""Notes for lecture 4 for class covering user input and some data structures"""
from typing import Optional

nums: list[int] = [1, 4, 5, 6]
letters: set[str] = {'a', 'b', 'c'}
#Sets cannot contain duplicates and aren't ordered

"""
Docstring example:

Description
Function x does this in order to get y and then also does z

Parameters
Phrase: str
    Small phrase of words to turn sarcastic

Returns
str
    Returns the sarcastic version of the str
None
    Can also return None

Errors
ValueError: if phrase is empty
"""

def get_number_or_none(num: str) -> Optional[int]:
    """Gets a number from the str or if its not a number returns None"""
    try:
        return int(num)
    except ValueError:
        return None

'''
self.assertEqual(4, 2 + 2)
with self.assertRaises(ValueError):
    get_number_or_none([1, 4, None])

self.assertTrue(1 + 1 < 3)
'''

with open('story.txt', 'r', encoding='utf-8') as file:
    for line in file.readlines():
        print(line)