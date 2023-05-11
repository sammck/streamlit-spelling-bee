import os
import urllib.request

from typing import Generator, Optional

DEFAULT_DICTIONARY_NAME = 'scrabble_words.txt'
DEFAULT_DICTIONARY_URL = 'https://raw.githubusercontent.com/jonbcard/scrabble-bot/master/src/dictionary.txt'

def data_dir() -> str:
  return os.path.join(os.path.dirname(__file__), 'data')

def dictionary_file(name: Optional[str]=None) -> str:
  if name is None:
    name = os.path.join(data_dir(), DEFAULT_DICTIONARY_NAME)
    if not os.path.exists(name):
      name = DEFAULT_DICTIONARY_URL
  if not (name.startswith('http:/') or name.startswith('https:/')):
    name = os.path.join(data_dir(), name)
  return name

def url_dictionary_words(dictionary_url: str=DEFAULT_DICTIONARY_URL) -> Generator[str, None, None]:
  with urllib.request.urlopen(dictionary_url) as r:
    for line in r:
      yield line.decode('utf8').strip().lower()

def file_dictionary_words(dictionary_name: str=DEFAULT_DICTIONARY_NAME) -> Generator[str, None, None]:
  with open(dictionary_file(dictionary_name)) as f:
    for line in f:
      yield line.strip().lower()

def dictionary_words(dictionary_name: Optional[str]=None) -> Generator[str, None, None]:
  pathname = dictionary_file(dictionary_name)
  if pathname.startswith('http:/') or pathname.startswith('https:/'):
    yield from url_dictionary_words(pathname)
  else:
    yield from file_dictionary_words(pathname)



