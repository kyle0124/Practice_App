import streamlit as st
import time

e = st.empty()

def hasClicked() :
    if 'clicked' in st.session_state.keys() and st.session_state['clicked'] :
        return True
    else :
        return False
    
if hasClicked() :
    with st.form(key='sample_form', clear_on_submit=False) :
        name = st.text_input('Input Name')
        age = st.slider('Select Age', 10, 90, 40)
        gender = st.radio('Select Gender', ['Male', 'Female'])
        submitted = st.form_submit_button('Submit')
        if submitted :
            e.write({'Name' : name, 
                     'Age' : age,
                     'Gender' : gender})
else :
    if st.button('Show Form') :
        st.session_state['clicked'] = True
        st.experimental_rerun()






















