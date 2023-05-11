#!/usr/bin/env python3

from typing import Optional, Iterable

import sys
import argparse

from spelling_bee import solve_spelling_bee, dictionary_words, is_pangram

def main():
    parser = argparse.ArgumentParser(description='Spelling Bee Solver')
    parser.add_argument('letters', type=str, help='The letters in the hive')
    parser.add_argument('--center', '-c', type=str, default='', help='The center letter. If not provided, the first letter is used')
    parser.add_argument('--dictionary', '-d', type=str, default='', help='The dictionary file. If not provided, the default dictionary is used')
    args = parser.parse_args()
    
    letters = args.letters
    center = args.center
    dictionary_file = args.dictionary
    word_list: Optional[Iterable[str]] = None if dictionary_file == '' else dictionary_words(dictionary_file)

    results = sorted(solve_spelling_bee(letters, first_letter=center, word_list=word_list))
    
    pangrams = [word for word in results if is_pangram(word, letters+center)]

    print('Pangrams:')
    for word in pangrams:
        print(f"   {word}")

    starting_two = ''
    for word in results:
      w2 = word[:2]
      if w2 != starting_two:
        starting_two = w2
        print()
        print(f'{starting_two.upper()}:')
        print("---")
      print(f'   {word}')

if __name__ == '__main__':
  main()
