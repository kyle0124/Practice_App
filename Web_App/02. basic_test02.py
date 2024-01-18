import streamlit as st
import pandas as pd

x = 1
y = 2

sample = {'Column_1' : [11, 22, 33],
          'Column_2' : ['aa', 'bb', 'cc'],
          'Column_3' : [True, False, True]}

df = pd.DataFrame(data=sample)

'_Text Text Text **Text**'
x
y
'DataFrame', df

# Markdown Color
':blue[Yellow]'
':red[Green]'
':green[White]'
':violet[Pink]'
':orange[Black]'

st.markdown("<span style='color:hotpink'>Violet</span>", unsafe_allow_html=True)

# Emoji

':sunglasses:'
':thumbsup:'
':100: score :100: :smile:'



