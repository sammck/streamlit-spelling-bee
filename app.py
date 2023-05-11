import os
import streamlit as st
import json
import logging

from app_static import all_words
from spelling_bee import solve_spelling_bee, is_pangram

logger = logging.getLogger(__name__)
logger.debug("app.py is reloading")

st.title("NYT Spelling Bee Helper")

# make sidebar wider.  the default is 21rem
#st.markdown(
#    f'''<style>
#        section[data-testid="stSidebar"] .css-ng1t4o {{width: 30rem;}}
#        section[data-testid="stSidebar"] .css-1d391kg {{width: 30rem;}}
#    </style>
#''',
#    unsafe_allow_html=True
#  )

letters = st.sidebar.text_input('Letters (center letter first)')

solve_button_pressed = st.sidebar.button('Solve', help="Press to generate solutions")

if solve_button_pressed:
    results = sorted(solve_spelling_bee(letters, word_list=all_words))
    pangrams = [word for word in results if is_pangram(word, letters)]
    with st.expander("Pangrams", expanded=False):
      st.text("\n".join(pangrams))
    while len(results) > 0:
      starting_two = results[0][:2]
      i = 0
      while i < len(results) and results[i][:2] == starting_two:
        i += 1
      with st.expander(starting_two.upper(), expanded=False):
        st.text("\n".join(results[:i]))
      results = results[i:]

logger.debug("app.py is done loading")
