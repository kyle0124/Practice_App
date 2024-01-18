import streamlit as st
import pandas as pd
import numpy as np
import time

# 1 (without parameter)

@st.cache_data
def getData1() :
    data = pd.read_csv('../data_web/data_iris.csv')
    time.sleep(5)
    return data

e1 = st.empty()

if st.button('Run', key=1) :
    data1 = getData1()
    e1.write(data1.head())

if st.button('Clear All Cache', key=2) :
    st.cache_data.clear()

''
'---'
''


# 2 (with parameter)
@st.cache_data
def getData2(age) :
    data = {'name' : 'Hong Gil Dong',
            'age' : age,
            'gender' : 'male'}
    time.sleep(5)
    return data

age = st.slider('Select age', 20, 25, 30)

e2 = st.empty()

if st.button('Run', key=3) :
    data2 = getData2(age)
    e2.write(data2)

if st.button('Clear All Cache', key=4) :
    st.cache_data.clear()




