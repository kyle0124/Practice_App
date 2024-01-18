import streamlit as st
import time

@st.cache_data
def getData(name, age, gender) :
    data = {'name' : name,
            'age' : age,
            'gender' : gender}
    time.sleep(5)
    return data

e1 = st.empty()

name1 = st.text_input('Input Name')
age1 = st.slider('Select Age', 10, 90, 40)
gender1 = st.radio('Select Gender', ['Male', 'Female'])

e1.write(getData(name1, age1, gender1))

''
'---'
''

e2 = st.empty()

with st.form(key='form1', clear_on_submit=False) :
    name2 = st.text_input('Input Name')
    age2 = st.slider('Select Age', 10, 90, 40)
    gender2 = st.radio('Select Gender', ['Male', 'Female'])
    submit = st.form_submit_button('Submit')
    if submit :
        e2.write(getData(name2, age2, gender2))

























