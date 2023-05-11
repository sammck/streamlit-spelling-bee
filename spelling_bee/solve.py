from typing import Iterable, Optional, Generator

import re

from.util import dictionary_words

def is_pangram(word: str, letters: str) -> bool:
  word = word.lower()
  letters = letters.lower()
  return all(letter in word for letter in letters)

def solve_spelling_bee(letters: str, first_letter: str='', word_list: Optional[Iterable[str]]=None) -> Generator[str, None, None]:
  if not word_list:
    word_list = dictionary_words()
  if first_letter == '':
    first_letter = letters[0]
  first_letter = first_letter.lower()
  letter_set = set(letters.lower())
  letter_set.add(first_letter)
  letters = ''.join(letter_set)
  if len(letters) != 7:
    raise ValueError('There must be exactly 7 letters including the center letter')
  pattern = re.compile(r'^[' + letters + r']+$')
  for word in word_list:
    word = word.lower()
    if len(word) >= 4 and first_letter in word and pattern.match(word):
      yield word
