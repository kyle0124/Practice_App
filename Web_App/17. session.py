import streamlit as st

if 'counter' not in st.session_state :
    st.session_state['counter'] = 0


count = st.empty()

col1, col2, _ = st.columns([1, 1, 5])

if col1.button('Add 1') :
    st.session_state['counter'] += 1

if col2.button('Clear') :
    st.session_state['counter'] = 0

count.write('Counter = {}'.format(st.session_state['counter']))


















